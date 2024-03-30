from typing import List

import inject

from dtos.global_message_dto import DeletedSuccess, ReturnMiddleware
from dtos.user_message_dto import RequestUserCreateMessageDTO, RequestUserUpdateMessageDTO, RequestUserUpdatePasswordMessageDTO
from middlewares.authenticate import auth_token, auth_token_with_permission
from services.user_service import UserService
from schemas.user import UserModel
from database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

user_router = APIRouter()

@user_router.post("/users", summary="Criar Usuário", response_model=UserModel)
def create(body: RequestUserCreateMessageDTO, db: Session = Depends(get_db), token_data: ReturnMiddleware = Depends(auth_token_with_permission(1))):
    try:
        service = UserService()
        user = service.create(body,db,token_data.user_id)
        db.commit()
        db.refresh(user)
        return user
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))



@user_router.get("/users/{user_id}", summary="Buscar Usuário pelo ID", response_model=UserModel)
def read(user_id: int, db: Session = Depends(get_db), token_data: ReturnMiddleware = Depends(auth_token_with_permission(3))):
    try:
        service = UserService()
        return service.get_id(user_id,db)
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))


@user_router.put("/users/{user_id}", summary="Alterar o Usuário pelo ID", response_model=UserModel)
def update(user_id: int, body: RequestUserUpdateMessageDTO, db: Session = Depends(get_db), token_data: ReturnMiddleware = Depends(auth_token_with_permission(4))):
    try:
        service = inject.instance(UserService)
        user = service.update(body,user_id,db,token_data.user_id)
        db.commit()
        db.refresh(user)
        return user
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))


@user_router.patch("/users/{user_id}/password", summary="Alterar a Senha do Usuário pelo ID", response_model=UserModel)
def update_password(user_id: int, body: RequestUserUpdatePasswordMessageDTO, db: Session = Depends(get_db), token_data: ReturnMiddleware = Depends(auth_token_with_permission(6))):
    try:
        service = UserService()
        user = service.update_password(body,user_id,db,token_data.user_id)
        db.commit()
        db.refresh(user)
        return user
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))

@user_router.delete("/users/{user_id}", summary="Deletar o usuário pelo Id", response_model=DeletedSuccess)
def delete(user_id: int, db: Session = Depends(get_db), token_data: ReturnMiddleware = Depends(auth_token_with_permission(5))):
    try:
        service = UserService()
        response = service.delete(user_id,db,token_data.user_id)
        db.commit()
        return response
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))

@user_router.get("/users", summary="Buscar todos os usuários", response_model=List[UserModel])
def get_all(db: Session = Depends(get_db), token_data: ReturnMiddleware = Depends(auth_token_with_permission(2))):
    try:
        service = UserService()
        return service.get_all(db)
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))