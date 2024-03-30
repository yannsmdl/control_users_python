
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import update, and_
from datetime import datetime, timedelta
from dtos.user_session_message_dto import RequestSessionMessageDTO
from interfaces.repository.iuser_session_repository import IUserSessionRepository
from models.user_session import UserSession
from schemas.user_session import UserSessionModel

class UserSessionRepository(IUserSessionRepository):
    def __init__(self):
        pass

    def get_by_user_id(self, user_id: int, db: Session)->List[UserSessionModel]:
        try:
            db_UserSession = db.query(UserSession).filter(UserSession.user_id == user_id, UserSession.disabled == False).first()
            return db_UserSession
        except Exception as error:
            db.rollback()
            raise error
        
    def get_by_token(self, token: str, db: Session)->UserSessionModel:
        try:
            db_UserSession = db.query(UserSession).filter(UserSession.token == token, UserSession.disabled == False).first()
            return db_UserSession
        except Exception as error:
            db.rollback()
            raise error

    def disable_sessions_by_user_id(self, user_id: int, db: Session)->None:
        try:
            db.execute(
                update(UserSession)
                .where(and_(UserSession.user_id == user_id, UserSession.disabled == False))
                .values(disabled=True)
            )
            return
        except Exception as error:
            db.rollback()
            raise error

    def refresh_session(self, id: int, db: Session)->None:
        try:
            db_UserSession = db.query(UserSession).filter(UserSession.id == id, UserSession.disabled == False).first()
            db_UserSession.update(db, expires_in = str(datetime.now() + timedelta(hours=1)))
            return
        except Exception as error:
            db.rollback()
            raise error

    def create(self, body: RequestSessionMessageDTO, db: Session)->None:
        try:
            db_UserSession = UserSession(user_id=body.user_id,token=body.token,expires_in=body.expires_in)
            db.add(db_UserSession)
            return db_UserSession
        except Exception as error:
            db.rollback()
            raise error
