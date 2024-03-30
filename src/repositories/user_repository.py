
from typing import List
from interfaces.repository.iuser_repository import IUserRepository
from dtos.global_message_dto import DeletedSuccess
from models.user import User
from sqlalchemy.orm import Session
from dtos.user_message_dto import RequestUserCreateMessageDTO, RequestUserUpdateMessageDTO, RequestUserUpdatePasswordMessageDTO
from schemas.user import UserModel

class UserRepository(IUserRepository):
    def __init__(self):
        pass

    def get_email(self, user_email: str, db: Session)->User:
        try:
            db_User = db.query(User).filter(User.email == user_email, User.deleted_by == None).first()
            return db_User
        except Exception as error:
            db.rollback()
            raise error

    def get_id(self, user_id: int, db: Session)->User:
        try:
            db_User = db.query(User).filter(User.id == user_id, User.deleted_by == None).first()
            return db_User
        except Exception as error:
            db.rollback()
            raise error

    def create(self, body: RequestUserCreateMessageDTO, db: Session, operation_user_id: int)->User:
        try:
            db_User = User(name=body.name, password=body.password, email=body.email, birth_date=body.birth_date, created_by=operation_user_id)
            db.add(db_User)
            return db_User
        except Exception as error:
            db.rollback()
            raise error
    
    def update(self, body: RequestUserUpdateMessageDTO, user_id: int, db: Session, operation_user_id: int)->User:
        try:
            db_User = db.query(User).filter(User.id == user_id, User.deleted_by == None).first()
            db_User.update(db, name=body.name, password=db_User.password, email=body.email, birth_date=body.birth_date, updated_by=operation_user_id)
            return db_User
        except Exception as error:
            db.rollback()
            raise error
        
    def update_password(self, body: RequestUserUpdatePasswordMessageDTO, user_id: int, db: Session, operation_user_id: int)->User:
        try:
            db_User = db.query(User).filter(User.id == user_id, User.deleted_by == None).first()            
            db_User.update(db, name=db_User.name, password=body.password, email=db_User.email, birth_date=db_User.birth_date, updated_by=operation_user_id)
            return db_User
        except Exception as error:
            db.rollback()
            raise error
        
    
    def delete(self, user_id: int, db: Session, operation_user_id: int)->DeletedSuccess:
        try:
            db_User = db.query(User).filter(User.id == user_id, User.deleted_by == None).first()
            db_User.self_delete(db, deleted_by=operation_user_id)
            return DeletedSuccess(
                message="User deleted successfully"
            )
        except Exception as error:
            db.rollback()
            raise error
        
    def get_all(self, db: Session)->List[User]:
        try:
            return db.query(User).filter(User.deleted_by == None).all()
        except Exception as error:
            db.rollback()
            raise error