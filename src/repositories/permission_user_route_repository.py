
from typing import List
from dtos.permission_user_route_message_dto import CreatePermissionUserRouteDTO
from interfaces.repository.ipermission_user_route_repository import IPermissionUserRouteRepository
from dtos.global_message_dto import DeletedSuccess
from models.permission_user_route import PermissionUserRoute
from sqlalchemy.orm import Session

class PermissionUserRouteRepository(IPermissionUserRouteRepository):
    def __init__(self):
        pass

    def get_id(self, permission_id: int, db: Session)->PermissionUserRoute:
        try:
            db_Permission = db.query(PermissionUserRoute).filter(PermissionUserRoute.id == permission_id, PermissionUserRoute.deleted_by == None).first()
            return db_Permission
        except Exception as error:
            db.rollback()
            raise error
        
    def get_by_user_id_and_route_id(self, user_id: int, route_id: int, db: Session)->PermissionUserRoute:
        try:
            db_Permission = db.query(PermissionUserRoute).filter(PermissionUserRoute.user_id == user_id, PermissionUserRoute.route_id == route_id, PermissionUserRoute.deleted_by == None).first()
            return db_Permission
        except Exception as error:
            db.rollback()
            raise error

    def get_by_user_id(self, user_id: int, db: Session)->List[PermissionUserRoute]:
        try:
            return db.query(PermissionUserRoute).filter(PermissionUserRoute.deleted_by == None, PermissionUserRoute.user_id == user_id).all()
        except Exception as error:
            db.rollback()
            raise error

    def delete(self, permission_id: int, db: Session, operation_user_id:int)->DeletedSuccess:
        try:
            db_Permission = db.query(PermissionUserRoute).filter(PermissionUserRoute.id == permission_id, PermissionUserRoute.deleted_by == None).first()
            db_Permission.self_delete(db, deleted_by=operation_user_id)
            return DeletedSuccess(
                message="User deleted successfully"
            )
        except Exception as error:
            db.rollback()
            raise error

    def create(self, body: CreatePermissionUserRouteDTO, db: Session, operation_user_id:int)->PermissionUserRoute:
        try:
            db_Permission = PermissionUserRoute(
                user_id = body.user_id, 
                route_id = body.route_id,
                created_by=operation_user_id)
            db.add(db_Permission)
            return db_Permission
        except Exception as error:
            db.rollback()
            raise error
