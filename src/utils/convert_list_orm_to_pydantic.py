from typing import List, Type
from pydantic import BaseModel

def sqlalchemy_to_pydantic(sqlalchemy_model) -> Type[BaseModel]:
    fields = {}
    for column in sqlalchemy_model.__table__.columns:
        fields[column.name] = (column.type.python_type, None)
    return type(f"{sqlalchemy_model.__name__}Pydantic", (BaseModel,), fields)

def convert_to_pydantic_list(sqlalchemy_objects: List, pydantic_model: Type[BaseModel]) -> List[BaseModel]:
    pydantic_objects = []
    for sqlalchemy_object in sqlalchemy_objects:
        pydantic_object = pydantic_model(**sqlalchemy_object.__dict__)
        pydantic_objects.append(pydantic_object)
    return pydantic_objects
