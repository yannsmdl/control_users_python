import os
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from dotenv import load_dotenv

from database import get_db
from dtos.global_message_dto import ReturnMiddleware
from schemas.permission_user_route import PermissionUserRouteModel
from services.permission_user_route_service import PermissionUserRouteService
from services.user_session_service import UserSessionService
from services.user_service import UserService
from sqlalchemy.orm import Session

from utils.convert_list_orm_to_pydantic import convert_to_pydantic_list
load_dotenv()

# Chave secreta para assinar e verificar tokens JWT
SECRET_KEY = os.environ.get("SECRET_TOKEN")
ALGORITHM = "HS256"

# Criando uma instância de HTTPBearer
bearer_scheme = HTTPBearer()

def auth_token_with_permission(route_id: int):
    def _auth_token(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()), db: Session = Depends(get_db))->ReturnMiddleware:
        return auth_token(credentials, db)
    
    def _verify_access_route(route_id: int, permissions: List[str]):
        return verify_access_route(route_id, permissions)
    
    def _middleware(token_data: ReturnMiddleware = Depends(_auth_token)):
        if not _verify_access_route(route_id, token_data.permissions):
            raise HTTPException(status_code=401, detail="Usuário não possui permissão para essa rota")
        return token_data
    
    return _middleware

def verify_access_route(route_id: int, permissions: List[PermissionUserRouteModel])->bool:
    for permission in permissions:
        if route_id == permission.route_id:
            return True
    return False

def auth_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), db: Session = Depends(get_db))->ReturnMiddleware:
    token = credentials.credentials
    try:
        token = token.split()[-1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_service = UserService()
        user_service.get_id(payload.get('subject'),db)
        user_session_service = UserSessionService()
        user_session = user_session_service.get_by_token(token,db)
        user_session_service.refresh(user_session.id,db)
        permission_user_route_service = PermissionUserRouteService()
        permissions_user = permission_user_route_service.get_by_user_id(payload.get("subject"),db)
        permission_user_route_models = convert_to_pydantic_list(permissions_user, PermissionUserRouteModel)
        db.commit()

        return ReturnMiddleware(
            user_id=int(payload.get("subject")),
            permissions=permission_user_route_models
        )
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
