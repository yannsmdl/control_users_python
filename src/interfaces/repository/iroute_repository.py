from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session

from dtos.global_message_dto import DeletedSuccess
from dtos.route_message_dto import RequestRouteCreateMessageDTO, RequestRouteUpdateMessageDTO
from models.route import Route
from schemas.route import RouteModel


class IRouteRepository(ABC):
    @abstractmethod
    def get_id(self, route_id: int, db: Session)->Route:
        pass

    @abstractmethod
    def get_by_path_and_method(self, path: str, method: str, db: Session)->Route:
        pass

    @abstractmethod
    def create(self, body: RequestRouteCreateMessageDTO, db: Session, operation_route_id: int)->Route:
        pass

    @abstractmethod
    def update(self, body: RequestRouteUpdateMessageDTO, route_id: int, db: Session, operation_route_id: int)->Route:
        pass
    
    @abstractmethod
    def delete(self, route_id: int, db: Session, operation_route_id: int)->DeletedSuccess:
        pass

    @abstractmethod
    def get_all(self, db: Session)->List[Route]:
        pass
