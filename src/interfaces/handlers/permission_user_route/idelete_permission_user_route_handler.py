from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from dtos.global_message_dto import DeletedSuccess

class IDeletePermissionUserRouteHandler(ABC):
    @abstractmethod
    def execute(self, permission_id: int, db: Session, operation_user_id:int)->DeletedSuccess:
        pass