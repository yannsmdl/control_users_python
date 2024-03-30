from abc import ABC, abstractmethod
from typing import List
import inject
from sqlalchemy.orm import Session

from dtos.permission_user_route_message_dto import CreatePermissionUserRouteDTO, RequestPermissionUserRouteCreateMessageDTO
from interfaces.handlers.permission_user_route.icreate_permission_user_route_handler import ICreatePermissionUserRouteHandler
from interfaces.repository.ipermission_user_route_repository import IPermissionUserRouteRepository
from interfaces.repository.iroute_repository import IRouteRepository
from interfaces.repository.iuser_repository import IUserRepository
from models.permission_user_route import PermissionUserRoute

class CreatePermissionUserRouteHandler(ICreatePermissionUserRouteHandler):
    _permission_user_route_repository: IPermissionUserRouteRepository
    _user_repository: IUserRepository
    _route_repository: IRouteRepository

    @inject.autoparams()
    def __init__(
        self,
        permission_user_route_repository: IPermissionUserRouteRepository,
        user_repository: IUserRepository,
        route_repository: IRouteRepository
    ) -> None:
        self._permission_user_route_repository = permission_user_route_repository()
        self._user_repository = user_repository()
        self._route_repository = route_repository()

    def execute(self, body: RequestPermissionUserRouteCreateMessageDTO, db: Session, operation_user_id:int)->List[PermissionUserRoute]:
        user = self._user_repository.get_id(body.user_id,db)
        if not user:
            raise Exception("Usuário não existe")
        
        list_permissions: List[PermissionUserRoute] = []
        for route_id in body.list_routes:
            user_permission = self._permission_user_route_repository.get_by_user_id_and_route_id(
                body.user_id,
                route_id,
                db
            )
            if not user_permission:
                route = self._route_repository.get_id(route_id,db)
                if not route:
                    raise Exception(f"Rota de id {str(route_id)} não existe")
                body_create: CreatePermissionUserRouteDTO = CreatePermissionUserRouteDTO(
                    route_id=route_id,
                    user_id=body.user_id
                )
                user_permission = self._permission_user_route_repository.create(
                    body_create,
                    db,
                    operation_user_id
                )
            list_permissions.append(user_permission)
        return list_permissions