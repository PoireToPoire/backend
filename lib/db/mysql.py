from configparser import ConfigParser

from fastapi.security.http import HTTPBasicCredentials
from lib.constants import INI_FILE_PATH
from lib.db.queries import Query
from lib.models.user import User
import mysql.connector


class Database:
    _passwd: str
    _host: str
    _name: str
    _user: str

    def __init__(self, name: str, user: str, passwd: str, db_host: str):
        for arg in [name, user, passwd, db_host]:
            if not isinstance(arg, str):
                raise TypeError(f"str type was expected, got {type(arg)}")
        self._host = db_host
        self._passwd = passwd
        self._name = name
        self._user = user
        self.db = mysql.connector.connect(
            port=3306,
            host=self._host,
            user=self._user,
            password=self._passwd,
            database=self._name,
            auth_plugin="mysql_native_password"
        )
        self.cursor = self.db.cursor()

    def fetch_one(self, sql_query: str):
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()[0]

    def fetch_all(self, sql_query: str):
        self.cursor.execute(sql_query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.db.close()
        
    def is_user_registred(self, email: str, passwd: str):
        return False if self.fetch_all(Query.login(email, passwd)) == [] else True

    def find_user_by_id(self, user_id: str):
        return self.fetch_one(Query.USER_BY_ID(user_id))

    def find_post_by_id(self, post_id: str):
        return self.fetch_one(Query.POST_BY_ID(post_id))

    def find_user_by_email(self, email: str):
        return self.fetch_one(Query.USER_BY_EMAIL(email))


    # def update_user_by_id(self, user_id: str, new_user: User):
    #     return self.cursor.execute(Query.update_user(
    #         user_id, 
    #         name=new_user.name,
    #         age=new_user.age,
    #         gender=new_user.gender,
    #         status=new_user.is_connected,
    #         )
    #     )
    
    def insert_user(self, new_user: User):
        self.cursor.execute(Query.create_user(new_user))
        self.db.commit()
        return self.cursor.rowcount

def mysql_connection():
    config = ConfigParser()
    config.read(INI_FILE_PATH)
    mysql_conf = config['mysql']

    return Database(
        name=mysql_conf['db_name'],
        user=mysql_conf['db_user'],
        passwd=mysql_conf['db_passwd'],
        db_host=mysql_conf['db_host']
    )
