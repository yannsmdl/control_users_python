from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from dtos.user_message_dto import RequestUserUpdatePasswordMessageDTO
from models.user import User


class IUpdatePasswordUserHandler(ABC):
    @abstractmethod
    def execute(self, body: RequestUserUpdatePasswordMessageDTO, user_id: int, db: Session, operation_user_id: int)->User:
        pass