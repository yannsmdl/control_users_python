import bcrypt
import inject
from sqlalchemy.orm import Session

from dtos.user_message_dto import RequestUserUpdateMessageDTO, RequestUserUpdatePasswordMessageDTO
from interfaces.handlers.user.iupdate_password_user_handler import IUpdatePasswordUserHandler
from interfaces.repository.iuser_repository import IUserRepository
from models.user import User


class UpdatePasswordUserHandler(IUpdatePasswordUserHandler):
    _user_repository: IUserRepository = None
    
    @inject.autoparams()
    def __init__(
        self,
        user_repository: IUserRepository
    ) -> None:
        self._user_repository = user_repository()
        
    def execute(self,body: RequestUserUpdatePasswordMessageDTO, user_id: int, db: Session, operation_user_id: int)->User:
        user = self._user_repository.get_id(user_id,db)
        if not user:
            raise Exception("Usuário não existe")
        
        password = bcrypt.hashpw(body.password.encode('utf-8'), bcrypt.gensalt(8))
        body.password = password.decode('utf-8')
        return self._user_repository.update_password(body,user_id,db,operation_user_id)