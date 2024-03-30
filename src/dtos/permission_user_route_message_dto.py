from typing import List
from pydantic import BaseModel

class RequestPermissionUserRouteCreateMessageDTO(BaseModel):
    user_id: int
    list_routes: List[int]

class CreatePermissionUserRouteDTO(BaseModel):
    user_id: int
    route_id: int

class RequestsCopyPermissionUserRouteMessageDTO(BaseModel):
    paste_user_id: int
    copy_user_id: int