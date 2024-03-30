
from typing import List
from interfaces.repository.iroute_repository import IRouteRepository
from dtos.global_message_dto import DeletedSuccess
from models.route import Route
from sqlalchemy.orm import Session
from dtos.route_message_dto import RequestRouteCreateMessageDTO, RequestRouteUpdateMessageDTO
from schemas.route import RouteModel

class RouteRepository(IRouteRepository):
    def __init__(self):
        pass

    def get_by_path_and_method(self, path: str, method: str, db: Session)->Route:
        try:
            db_Route = db.query(Route).filter(Route.path == path, Route.method == method, Route.deleted_by == None).first()
            return db_Route
        except Exception as error:
            db.rollback()
            raise error
        
    def get_id(self, route_id: int, db: Session)->Route:
        try:
            db_Route = db.query(Route).filter(Route.id == route_id, Route.deleted_by == None).first()
            return db_Route
        except Exception as error:
            db.rollback()
            raise error

    def create(self, body: RequestRouteCreateMessageDTO, db: Session, operation_route_id: int)->Route:
        try:
            db_Route = Route(name=body.name, path=body.path, method=body.method, created_by=operation_route_id)
            db.add(db_Route)
            return db_Route
        except Exception as error:
            db.rollback()
            raise error
    
    def update(self, body: RequestRouteUpdateMessageDTO, route_id: int, db: Session, operation_route_id: int)->Route:
        try:
            db_Route = db.query(Route).filter(Route.id == route_id, Route.deleted_by == None).first()
            db_Route.update(db, name=body.name, path=db_Route.path, method=body.method, updated_by=operation_route_id)
            return db_Route
        except Exception as error:
            db.rollback()
            raise error
        
    def delete(self, route_id: int, db: Session, operation_route_id: int)->DeletedSuccess:
        try:
            db_Route = db.query(Route).filter(Route.id == route_id, Route.deleted_by == None).first()
            db_Route.self_delete(db, deleted_by=operation_route_id)
            return DeletedSuccess(
                message="Route deleted successfully"
            )
        except Exception as error:
            db.rollback()
            raise error
        
    def get_all(self, db: Session)->List[Route]:
        try:
            return db.query(Route).filter(Route.deleted_by == None).all()
        except Exception as error:
            db.rollback()
            raise error