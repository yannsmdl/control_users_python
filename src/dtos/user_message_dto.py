from datetime import date
from typing import Optional
from pydantic import BaseModel

class RequestUserCreateMessageDTO(BaseModel):
    name: str
    password: str
    email: str
    birth_date: date

class RequestUserUpdateMessageDTO(BaseModel):
    name: Optional[str]
    email: Optional[str]
    birth_date: Optional[date]


class RequestUserUpdatePasswordMessageDTO(BaseModel):
    password: str