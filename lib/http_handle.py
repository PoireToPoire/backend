from fastapi import HTTPException
from contextlib import contextmanager

from fastapi_jwt_auth.exceptions import InvalidHeaderError

@contextmanager
def handle_errors():
    try:
        yield
    except Exception as err:
        if isinstance(err, IndexError):
            raise HTTPException(status_code=404, detail=err)
        elif isinstance(err, InvalidHeaderError):
            raise HTTPException(status_code=422, detail="Invalid JWT")
        else:
            raise HTTPException(status_code=500, detail=err)    
