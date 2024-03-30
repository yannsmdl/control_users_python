

from typing import List
from pydantic import BaseModel

from schemas.permission_user_route import PermissionUserRouteModel


class DeletedSuccess(BaseModel):
    message: str

class ReturnMiddleware(BaseModel):
    user_id: int
    permissions: List[PermissionUserRouteModel]