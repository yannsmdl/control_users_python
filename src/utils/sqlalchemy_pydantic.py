from datetime import date, datetime
from typing import Optional, Type, Any, Tuple
from pydantic import BaseModel, create_model
from sqlalchemy import inspect, Column
from sqlalchemy.orm import DeclarativeMeta
from sqlalchemy.types import Integer as SA_Integer, String as SA_String, Boolean as SA_Boolean, DateTime as SA_DateTime, Date as SA_Date


def sqlalchemy_to_pydantic(sqlalchemy_model: DeclarativeMeta) -> Type[BaseModel]:
    sqlalchemy_mapper = inspect(sqlalchemy_model)
    columns = sqlalchemy_mapper.columns

    fields = {}
    for column_name, column in columns.items():
        field_type, default_value = sqlalchemy_type_to_pydantic_type(column)
        fields[column_name] = (field_type, default_value)

    pydantic_model = create_model(
        f"{sqlalchemy_model.__name__}Pydantic",
        **fields
    )

    return pydantic_model


def sqlalchemy_type_to_pydantic_type(column: Column) -> Tuple[Type, Optional[Any]]:
    python_type = type(column.type)
    default_value = None

    if python_type == SA_Integer:
        field_type = Optional[int]
    elif python_type == SA_String:
        field_type = Optional[str]
    elif python_type == SA_Boolean:
        field_type = Optional[bool]
    elif python_type == SA_DateTime:
        field_type = Optional[datetime]
    elif python_type == SA_Date:
        field_type = Optional[date]
    else:
        field_type = Any

    return field_type, default_value