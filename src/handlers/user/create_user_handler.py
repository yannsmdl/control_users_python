import bcrypt
import inject
from sqlalchemy.orm import Session

from dtos.user_message_dto import RequestUserCreateMessageDTO
from interfaces.handlers.user.icreate_user_handler import ICreateUserHandler
from interfaces.repository.iuser_repository import IUserRepository
from models.user import User


class CreateUserHandler(ICreateUserHandler):
    _user_repository: IUserRepository = None

    @inject.autoparams()
    def __init__(
        self,
        user_repository: IUserRepository
    ) -> None:
        self._user_repository = user_repository()
        
    def execute(self, body: RequestUserCreateMessageDTO, db: Session, operation_user_id: int)->User:
        user = self._user_repository.get_email(body.email,db)
        if user:
            raise Exception("Usuário já existe")
        password = bcrypt.hashpw(body.password.encode('utf-8'), bcrypt.gensalt(8))
        body.password = password.decode('utf-8')
        return self._user_repository.create(body,db,operation_user_id)