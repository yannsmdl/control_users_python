from models.permission_user_route import PermissionUserRoute
from utils.sqlalchemy_pydantic import sqlalchemy_to_pydantic
    
PydanticPermissionUserRoute = sqlalchemy_to_pydantic(PermissionUserRoute)

class PermissionUserRouteModel(PydanticPermissionUserRoute):
    pass