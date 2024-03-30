from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session

from dtos.permission_user_route_message_dto import RequestPermissionUserRouteCreateMessageDTO
from models.permission_user_route import PermissionUserRoute

class ICreatePermissionUserRouteHandler(ABC):
    @abstractmethod
    def execute(self, body: RequestPermissionUserRouteCreateMessageDTO, db: Session, operation_user_id:int)->List[PermissionUserRoute]:
        pass