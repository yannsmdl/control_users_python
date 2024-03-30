from pydantic import BaseModel
from models.user import User
from utils.sqlalchemy_pydantic import sqlalchemy_to_pydantic


PydanticUser = sqlalchemy_to_pydantic(User)

class UserModel(PydanticUser):
    pass