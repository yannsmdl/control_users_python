from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session

from dtos.global_message_dto import DeletedSuccess
from dtos.permission_user_route_message_dto import CreatePermissionUserRouteDTO
from models.permission_user_route import PermissionUserRoute


class IPermissionUserRouteRepository(ABC):
    @abstractmethod
    def get_id(self, permission_id: int, db: Session)->PermissionUserRoute:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: int, db: Session)->List[PermissionUserRoute]:
        pass

    @abstractmethod
    def get_by_user_id_and_route_id(self, user_id: int, route_id: int, db: Session)->PermissionUserRoute:
        pass

    @abstractmethod
    def delete(self, permission_id: int, db: Session, operation_user_id:int)->DeletedSuccess:
        pass

    @abstractmethod
    def create(self, body: CreatePermissionUserRouteDTO, db: Session, operation_user_id:int)->PermissionUserRoute:
        pass
