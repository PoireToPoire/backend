from socket import gethostname
from os import path

API_HOST: str = gethostname()
INI_FILE_PATH: str = path.abspath(path.join(path.dirname(path.dirname(__file__)), "db/db.ini"))
STATIC_PATH: str = path.abspath(path.join(path.dirname(path.dirname(path.dirname(__file__))), "static"))