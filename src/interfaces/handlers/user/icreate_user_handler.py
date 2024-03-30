from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from dtos.user_message_dto import RequestUserCreateMessageDTO
from models.user import User


class ICreateUserHandler(ABC):
    @abstractmethod
    def execute(self, body: RequestUserCreateMessageDTO, db: Session, operation_user_id: int)->User:
        pass