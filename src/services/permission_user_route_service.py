
from typing import List
import inject
from interfaces.handlers.permission_user_route.icopy_user_permission_user_route_handler import ICopyUserPermissionUserRouteHandler
from interfaces.handlers.permission_user_route.icreate_permission_user_route_handler import ICreatePermissionUserRouteHandler
from interfaces.handlers.permission_user_route.idelete_permission_user_route_handler import IDeletePermissionUserRouteHandler
from interfaces.repository.ipermission_user_route_repository import IPermissionUserRouteRepository
from dtos.global_message_dto import DeletedSuccess
from models.permission_user_route import PermissionUserRoute
from sqlalchemy.orm import Session
from dtos.permission_user_route_message_dto import RequestPermissionUserRouteCreateMessageDTO


class PermissionUserRouteService:
    _permission_user_route_repository: IPermissionUserRouteRepository
    _create_permission_user_route_handler: ICreatePermissionUserRouteHandler
    _delete_permission_user_route_handler: IDeletePermissionUserRouteHandler
    _copy_user_permission_user_route_handler : ICopyUserPermissionUserRouteHandler

    @inject.autoparams()
    def __init__(
        self,
        permission_user_route_repository: IPermissionUserRouteRepository,
        create_permission_user_route_handler: ICreatePermissionUserRouteHandler,
        delete_permission_user_route_handler: IDeletePermissionUserRouteHandler,
        copy_user_permission_user_route_handler : ICopyUserPermissionUserRouteHandler
    ) -> None:
        self._permission_user_route_repository = permission_user_route_repository()
        self._create_permission_user_route_handler = create_permission_user_route_handler()
        self._delete_permission_user_route_handler = delete_permission_user_route_handler()
        self._copy_user_permission_user_route_handler = copy_user_permission_user_route_handler()

    def get_id(self, permission_user_route_id: int, db: Session)->PermissionUserRoute:
        permission_user_route = self._permission_user_route_repository.get_id(permission_user_route_id,db)
        if not permission_user_route:
            raise Exception("Usuário não encontrado")
        return permission_user_route

    def create(self, body: RequestPermissionUserRouteCreateMessageDTO, db: Session, operation_permission_user_route_id: int)->List[PermissionUserRoute]:
        return self._create_permission_user_route_handler.execute(body,db,operation_permission_user_route_id)
    
    def copy_permission_user(self, paste_user_id: int, copy_user_id: int, db: Session, operation_user_id:int)->List[PermissionUserRoute]:
        return self._copy_user_permission_user_route_handler.execute(paste_user_id,copy_user_id,db,operation_user_id)

    def delete(self, permission_user_route_id: int, db: Session, operation_permission_user_route_id: int)->DeletedSuccess:
        return self._delete_permission_user_route_handler.execute(permission_user_route_id,db,operation_permission_user_route_id)

    def get_by_user_id(self, user_id: int, db: Session)->List[PermissionUserRoute]:
        return self._permission_user_route_repository.get_by_user_id(user_id, db)
