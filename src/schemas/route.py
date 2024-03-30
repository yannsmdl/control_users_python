from models.route import Route
from utils.sqlalchemy_pydantic import sqlalchemy_to_pydantic

    
PydanticRoute = sqlalchemy_to_pydantic(Route)

class RouteModel(PydanticRoute):
    pass