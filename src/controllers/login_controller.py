from dtos.login_message_dto import RequestLoginMessageDTO, ResponseLoginMessageDTO
from services.login_service import LoginService
from services.user_service import UserService
from database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

login_router = APIRouter()

@login_router.post("/login", summary="Autenticar", response_model=ResponseLoginMessageDTO)
def create(body: RequestLoginMessageDTO, db: Session = Depends(get_db)):
    try:
        service = LoginService()
        login = service.autenticate(body,db)
        db.commit()
        return login
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))
