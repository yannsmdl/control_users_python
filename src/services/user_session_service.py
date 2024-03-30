import inject
from sqlalchemy.orm import Session
from interfaces.repository.iuser_session_repository import IUserSessionRepository
from schemas.user_session import UserSessionModel




class UserSessionService:
    _user_session_repository: IUserSessionRepository
    @inject.autoparams()
    def __init__(
        self,
        user_session_repository: IUserSessionRepository
    ) -> None:
        self._user_session_repository = user_session_repository()

    def get_by_token(self, token: str, db: Session)->UserSessionModel:
        user_session = self._user_session_repository.get_by_token(token,db)
        if not user_session:
            raise Exception("Sessao não encontrada")
        return user_session
    
    def refresh(self, id: int , db: Session)->None:
        return self._user_session_repository.refresh_session(id,db)