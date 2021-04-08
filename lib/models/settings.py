from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = "cubes-api-secret-key"
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_csrf_protect: bool = False
    authjwt_cookie_secure: bool = False
    authjwt_cookie_samesite: str = 'lax'