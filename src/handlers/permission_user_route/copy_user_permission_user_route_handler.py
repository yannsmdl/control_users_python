from abc import ABC, abstractmethod
from typing import List
import inject
from sqlalchemy.orm import Session

from dtos.permission_user_route_message_dto import CreatePermissionUserRouteDTO
from interfaces.handlers.permission_user_route.icopy_user_permission_user_route_handler import ICopyUserPermissionUserRouteHandler
from interfaces.repository.ipermission_user_route_repository import IPermissionUserRouteRepository
from interfaces.repository.iuser_repository import IUserRepository
from models.permission_user_route import PermissionUserRoute

class CopyUserPermissionUserRouteHandler(ICopyUserPermissionUserRouteHandler):
    _permission_user_route_repository: IPermissionUserRouteRepository
    _user_repository: IUserRepository

    @inject.autoparams()
    def __init__(
        self,
        permission_user_route_repository: IPermissionUserRouteRepository,
        user_repository: IUserRepository
    ) -> None:
        self._permission_user_route_repository = permission_user_route_repository()
        self._user_repository = user_repository()
        
    def execute(self, paste_user_id: int, copy_user_id: int, db: Session, operation_user_id:int)->List[PermissionUserRoute]:
        copy_user = self._user_repository.get_id(copy_user_id,db)
        if not copy_user:
            raise Exception("Usuário modelo para copia de permissao não existe")
        
        paste_user = self._user_repository.get_id(paste_user_id,db)
        if not paste_user:
            raise Exception("Não existe o usuário que receberá as permissões")
        
        permissions_user_copy = self._permission_user_route_repository.get_by_user_id(copy_user_id,db)
        if len(permissions_user_copy)<=0:
            raise Exception("O usuário modelo para copia de permissões, não possui nenhuma permissão")
        
        list_permissions: List[PermissionUserRoute] = []
        for permission in permissions_user_copy:
            user_permission = self._permission_user_route_repository.get_by_user_id_and_route_id(
                paste_user_id,
                permission.route_id,
                db
            )
            if not user_permission:
                body: CreatePermissionUserRouteDTO = CreatePermissionUserRouteDTO(
                    route_id=permission.route_id,
                    user_id=paste_user_id
                )
                user_permission = self._permission_user_route_repository.create(
                    body,
                    db,
                    operation_user_id
                )
            list_permissions.append(user_permission)
        return list_permissions