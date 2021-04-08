from fastapi import APIRouter, Depends, HTTPException, Cookie
from fastapi_jwt_auth import AuthJWT
from fastapi.responses import JSONResponse
from lib.models import Credentials, User
from lib.db.mysql import mysql_connection, Database

router = APIRouter(tags=["auth"])


@router.post("/signin")
def user_create(user: User, db: Database = Depends(mysql_connection)):
    if not db.is_user_registred(user.email, user.passwd):
        resp = {"status": db.insert_user(user)}
    else:
        resp = {"status": "user already exists"}
    return resp

@router.post("/login")
def user_login(credentials: Credentials, Authorize: AuthJWT = Depends(), db: Database = Depends(mysql_connection)):
    Authorize.jwt_optional()
    print(credentials)
    if not db.is_user_registred(credentials.email, credentials.password):
        raise HTTPException(status_code=401, detail="Bad credentials")
    access_token = Authorize.create_access_token(subject=credentials.email)
    refresh_token = Authorize.create_refresh_token(subject=credentials.email)
    response = JSONResponse({"user_id": db.find_user_by_email(credentials.email)[0]})
    Authorize.set_access_cookies(access_token, response)
    Authorize.set_refresh_cookies(refresh_token, response)
    return response


@router.delete('/logout')
def logout(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    Authorize.unset_jwt_cookies()
    response = JSONResponse({"detail": "Successfully logout"})
    response.unset_cookie()
    return response
