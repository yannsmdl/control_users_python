from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from dtos.user_message_dto import RequestUserUpdateMessageDTO
from models.user import User


class IUpdateUserHandler(ABC):
    @abstractmethod
    def execute(self, body: RequestUserUpdateMessageDTO, user_id: int, db: Session, operation_user_id: int)->User:
        pass