from abc import ABC, abstractmethod
import bcrypt
import inject
from sqlalchemy.orm import Session

from dtos.global_message_dto import DeletedSuccess
from interfaces.handlers.user.idelete_user_handler import IDeleteUserHandler
from interfaces.repository.iuser_repository import IUserRepository
from models.user import User


class DeleteUserHandler(IDeleteUserHandler):
    _user_repository: IUserRepository = None

    @inject.autoparams()
    def __init__(
        self,
        user_repository: IUserRepository
    ) -> None:
        self._user_repository = user_repository()
        
    def execute(self, user_id: int, db: Session, operation_user_id: int)->DeletedSuccess:
        user = self._user_repository.get_id(user_id,db)
        if not user:
            raise Exception("Usuário não existe")
        return self._user_repository.delete(user_id,db,operation_user_id)