from models.user_session import UserSession
from utils.sqlalchemy_pydantic import sqlalchemy_to_pydantic

PydanticUserSession = sqlalchemy_to_pydantic(UserSession)

class UserSessionModel(PydanticUserSession):
    pass