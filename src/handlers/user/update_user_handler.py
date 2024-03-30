import inject
from sqlalchemy.orm import Session

from dtos.user_message_dto import RequestUserUpdateMessageDTO
from interfaces.handlers.user.iupdate_user_handler import IUpdateUserHandler
from interfaces.repository.iuser_repository import IUserRepository
from models.user import User


class UpdateUserHandler(IUpdateUserHandler):
    _user_repository: IUserRepository = None
    
    @inject.autoparams()
    def __init__(
        self,
        user_repository: IUserRepository
    ) -> None:
        self._user_repository = user_repository()
        
    def execute(self,body: RequestUserUpdateMessageDTO, user_id: int, db: Session, operation_user_id: int)->User:
        user = self._user_repository.get_id(user_id,db)
        if not user:
            raise Exception("Usuário não existe")
        
        if body.email and user.email != body.email:
            user_email = self._user_repository.get_email(body.email,db)
            if user_email:
                raise Exception("Email informado já existe")

        body.name = body.name if body.name else user.name
        body.email = body.email if body.email else user.email
        body.birth_date = body.birth_date if body.birth_date else user.birth_date

        return self._user_repository.update(body,user_id,db,operation_user_id)