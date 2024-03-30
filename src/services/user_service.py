
from typing import List
import inject
from interfaces.handlers.user.icreate_user_handler import ICreateUserHandler
from interfaces.handlers.user.idelete_user_handler import IDeleteUserHandler
from interfaces.handlers.user.iupdate_password_user_handler import IUpdatePasswordUserHandler
from interfaces.handlers.user.iupdate_user_handler import IUpdateUserHandler
from interfaces.repository.iuser_repository import IUserRepository
from dtos.global_message_dto import DeletedSuccess
from models.user import User
from sqlalchemy.orm import Session
from dtos.user_message_dto import RequestUserCreateMessageDTO, RequestUserUpdateMessageDTO, RequestUserUpdatePasswordMessageDTO


class UserService:
    _user_repository: IUserRepository
    _update_user_handler: IUpdateUserHandler
    _create_user_handler: ICreateUserHandler
    _update_passowrd_user_handler: IUpdatePasswordUserHandler
    _delete_user_handler: IDeleteUserHandler

    @inject.autoparams()
    def __init__(
        self,
        user_repository: IUserRepository,
        update_user_handler: IUpdateUserHandler,
        create_user_handler: ICreateUserHandler,
        update_passowrd_user_handler: IUpdatePasswordUserHandler,
        delete_user_handler: IDeleteUserHandler
    ) -> None:
        self._user_repository = user_repository()
        self._update_user_handler = update_user_handler()
        self._create_user_handler = create_user_handler()
        self._update_passowrd_user_handler = update_passowrd_user_handler()
        self._delete_user_handler = delete_user_handler()

    def get_id(self, user_id: int, db: Session)->User:
        user = self._user_repository.get_id(user_id,db)
        if not user:
            raise Exception("Usuário não encontrado")
        return user

    def create(self, body: RequestUserCreateMessageDTO, db: Session, operation_user_id: int)->User:
        return self._create_user_handler.execute(body,db,operation_user_id)

    def update(self, body: RequestUserUpdateMessageDTO, user_id: int, db: Session, operation_user_id: int)->User:
        return self._update_user_handler.execute(body,user_id,db,operation_user_id)
    
    def update_password(self, body: RequestUserUpdatePasswordMessageDTO, user_id: int, db: Session, operation_user_id: int)->User:
        return self._update_passowrd_user_handler.execute(body,user_id,db,operation_user_id)

    def delete(self, user_id: int, db: Session, operation_user_id: int)->DeletedSuccess:
        return self._delete_user_handler.execute(user_id,db,operation_user_id)

    def get_all(self, db: Session)->List[User]:
        return self._user_repository.get_all(db)
