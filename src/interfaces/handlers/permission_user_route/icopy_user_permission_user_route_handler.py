from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session

from models.permission_user_route import PermissionUserRoute

class ICopyUserPermissionUserRouteHandler(ABC):
    @abstractmethod
    def execute(self, paste_user_id: int, copy_user_id: int, db: Session, operation_user_id:int)->List[PermissionUserRoute]:
        pass