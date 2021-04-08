from lib.models.user import User

class Query:
    USER_BY_ID = lambda user_id : f"SELECT * FROM user WHERE id={user_id} LIMIT 1"
    POST_BY_ID = lambda post_id : f"SELECT * FROM post WHERE id={post_id} LIMIT 1"
    USER_BY_EMAIL = lambda email : f"SELECT id FROM user WHERE mail='{email}' LIMIT 1"

    @classmethod
    def login(cls, email: str, passwd: str):
        return f"SELECT id FROM user WHERE mail='{email}' AND password='{passwd}'"

    @classmethod
    def update_user(cls, user_id: str, **user):
        query = "UPDATE user SET" 
        for column in user:
            value = user[column]
            query += f" '{column}'='{value}',"
        query += f" WHERE user.id={user_id}"
        return query.replace(", WHERE", " WHERE")   
        
    @classmethod
    def create_user(cls, user: User, usertype: int = 1):
        return f"INSERT INTO user(firstname, lastname, password, mail, birthdate, gender, type) VALUES ('{user.firstname}', '{user.lastname}', '{user.passwd}', '{user.email}', '{user.bdate}', '{user.gender}', {usertype});"

