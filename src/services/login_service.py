import os
import jwt
import bcrypt
import inject
from sqlalchemy.orm import Session
from dtos.user_session_message_dto import RequestSessionMessageDTO
from interfaces.repository.iuser_session_repository import IUserSessionRepository
from datetime import datetime, timedelta
from dtos.login_message_dto import RequestLoginMessageDTO, ResponseLoginMessageDTO
from interfaces.repository.iuser_repository import IUserRepository




class LoginService:
    _user_repository: IUserRepository
    _user_session_repository: IUserSessionRepository

    @inject.autoparams()
    def __init__(
        self,
        user_repository: IUserRepository,
        user_session_repository: IUserSessionRepository
    ) -> None:
        self._user_repository = user_repository()
        self._user_session_repository = user_session_repository()

    def autenticate(self, body: RequestLoginMessageDTO, db: Session)->ResponseLoginMessageDTO:
        try:
            user = self._user_repository.get_email(body.email,db)
            password_digitada = body.password.encode('utf-8')
            password_bd = user.password.encode('utf-8')
            if not bcrypt.checkpw(password_digitada, password_bd):
                raise Exception("Senha incorreta")
            
            expires_in = datetime.now() + timedelta(hours=1)

            data_token = {
                "name":user.name,
                "email":user.email,
                "birth_date":user.birth_date.isoformat(),
                'subject': str(user.id),
                'expiresIn':'1h'
            }


            token = jwt.encode(data_token, os.environ.get('SECRET_TOKEN'), algorithm='HS256')

            self._user_session_repository.disable_sessions_by_user_id(user.id,db)

            data_create_token: RequestSessionMessageDTO = RequestSessionMessageDTO(
                user_id=user.id,
                token=token,
                expires_in=str(expires_in)
            )

            self._user_session_repository.create(data_create_token,db)

            return ResponseLoginMessageDTO(
                token=token,
                expires_in=str(expires_in)
            )


        except Exception as error:
            raise Exception ("Usuário ou password não existem")

