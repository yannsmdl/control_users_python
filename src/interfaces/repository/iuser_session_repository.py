from typing import List
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from schemas.user_session import UserSessionModel
from dtos.user_session_message_dto import RequestSessionMessageDTO


class IUserSessionRepository(ABC):
    @abstractmethod
    def get_by_user_id(self, user_id: int, db: Session)->List[UserSessionModel]:
        pass

    @abstractmethod
    def get_by_token(self, token: str, db: Session)->UserSessionModel:
        pass

    @abstractmethod
    def disable_sessions_by_user_id(self, user_id: int, db: Session)->None:
        pass

    @abstractmethod
    def refresh_session(self, id: int, db: Session)->None:
        pass

    @abstractmethod
    def create(self, body: RequestSessionMessageDTO, db: Session)->None:
        pass