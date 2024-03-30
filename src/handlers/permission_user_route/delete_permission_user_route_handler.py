import inject
from sqlalchemy.orm import Session

from dtos.global_message_dto import DeletedSuccess
from interfaces.handlers.permission_user_route.idelete_permission_user_route_handler import IDeletePermissionUserRouteHandler
from interfaces.repository.ipermission_user_route_repository import IPermissionUserRouteRepository

class DeletePermissionUserRouteHandler(IDeletePermissionUserRouteHandler):
    _permission_user_route_repository: IPermissionUserRouteRepository

    @inject.autoparams()
    def __init__(
        self,
        permission_user_route_repository: IPermissionUserRouteRepository
    ) -> None:
        self._permission_user_route_repository = permission_user_route_repository()
        
    def execute(self, permission_id: int, db: Session, operation_user_id:int)->DeletedSuccess:
        user = self._permission_user_route_repository.get_id(permission_id,db)
        if not user:
            raise Exception("Permissao não existe")
        return self._permission_user_route_repository.delete(permission_id,db,operation_user_id)