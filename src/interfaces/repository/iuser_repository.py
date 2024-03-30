from abc import ABC, abstractmethod
from typing import List
from sqlalchemy.orm import Session

from dtos.global_message_dto import DeletedSuccess
from dtos.user_message_dto import RequestUserCreateMessageDTO, RequestUserUpdateMessageDTO, RequestUserUpdatePasswordMessageDTO
from models.user import User
from schemas.user import UserModel


class IUserRepository(ABC):
    @abstractmethod
    def get_email(self, user_email: str, db: Session)->User:
        pass

    @abstractmethod
    def get_id(self, user_id: int, db: Session)->User:
        pass

    @abstractmethod
    def create(self, body: RequestUserCreateMessageDTO, db: Session, operation_user_id: int)->User:
        pass

    @abstractmethod
    def update(self, body: RequestUserUpdateMessageDTO, user_id: int, db: Session, operation_user_id: int)->User:
        pass
    
    @abstractmethod
    def delete(self, user_id: int, db: Session, operation_user_id: int)->DeletedSuccess:
        pass

    @abstractmethod
    def get_all(self, db: Session)->List[User]:
        pass

    @abstractmethod
    def update_password(self, body: RequestUserUpdatePasswordMessageDTO, user_id: int, db: Session, operation_user_id: int)->User:
        pass