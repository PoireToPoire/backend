import os

from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import InvalidHeaderError
from lib.constants import STATIC_PATH
from lib.db import mysql_connection
from lib.http_handle import handle_errors
from lib.models import User

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

db = mysql_connection()


@router.post("/{user_id}")
def update_user(user_id: int, user: User, Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    db.update_user_by_id(user_id, user)
    new_access_token = Authorize.create_access_token(subject=user.email)
    Authorize.set_access_cookies(new_access_token)
    return {"detail": "User data updated"}


@router.get("/{user_id}")
def read_user(user_id: int, Authorize: AuthJWT = Depends()):
    Authorize.jwt_optional()
    user = db.find_user_by_id(user_id)
    return {
        "id": user_id,
        "lastname": user[3],
        "firstname": user[4],
        "mail": user[5],
        "birthday": str(user[6]),
        "bio": user[7],
        "gender": user[8],
        "image_path": user[10],
    }


@router.get("/{user_id}/status")
def get_current_user(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        current_user_mail = Authorize.get_jwt_subject()
        user_id = db.find_user_by_email(current_user_mail)[0]
        return {"current_user":  current_user_mail, "id": user_id}
    except InvalidHeaderError:
        raise HTTPException(409, "Unknown user")


@router.post("/{user_id}/upload")
async def upload_file(new_file: UploadFile = File(...), Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    file_name = os.path.join(STATIC_PATH, new_file.filename.replace(" ", "-"))
    try:
        with open(file_name, 'wb+') as f:
            f.write(new_file.file.read())
            f.close()
    except Exception as e:
        return({
            "result": "Error",
            "error": e
        })
