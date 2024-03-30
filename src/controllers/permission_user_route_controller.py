from typing import List

import inject

from dtos.global_message_dto import DeletedSuccess, ReturnMiddleware
from dtos.permission_user_route_message_dto import RequestPermissionUserRouteCreateMessageDTO, RequestsCopyPermissionUserRouteMessageDTO
from middlewares.authenticate import auth_token, auth_token_with_permission
from services.permission_user_route_service import PermissionUserRouteService
from schemas.permission_user_route import PermissionUserRouteModel
from database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends

permission_user_route_router = APIRouter()

@permission_user_route_router.post("/permission_user_routes", summary="Criar permissoes de usuário", response_model=PermissionUserRouteModel)
def create(body: RequestPermissionUserRouteCreateMessageDTO, db: Session = Depends(get_db), token_data: ReturnMiddleware = Depends(auth_token_with_permission(8))):
    try:
        service = PermissionUserRouteService()
        permission_user_route = service.create(body, db, token_data.user_id)
        db.commit()
        db.refresh(permission_user_route)
        return permission_user_route
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))

@permission_user_route_router.post("/permission_user_routes/copy", summary="Copiar as permissoes de um usuário para colocar em outro", response_model=PermissionUserRouteModel)
def copy(body: RequestsCopyPermissionUserRouteMessageDTO, db: Session = Depends(get_db), token_data: ReturnMiddleware = Depends(auth_token_with_permission(7))):
    try:
        service = PermissionUserRouteService()
        permission_user_route = service.copy_permission_user(body.paste_user_id, body.copy_user_id, db, token_data.user_id)
        db.commit()
        db.refresh(permission_user_route)
        return permission_user_route
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))


@permission_user_route_router.get("/permission_user_routes/{permission_user_route_id}", summary="Buscar uma permissão pelo ID", response_model=PermissionUserRouteModel)
def read(permission_user_route_id: int, db: Session = Depends(get_db), token_data: ReturnMiddleware = Depends(auth_token_with_permission(9))):
    try:
        service = PermissionUserRouteService()
        return service.get_id(permission_user_route_id, db)
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))

@permission_user_route_router.delete("/permission_user_routes/{permission_user_route_id}", summary="Deletar uma permissão pelo ID", response_model=DeletedSuccess)
def delete(permission_user_route_id: int, db: Session = Depends(get_db), token_data: ReturnMiddleware = Depends(auth_token_with_permission(11))):
    try:
        service = PermissionUserRouteService()
        response = service.delete(permission_user_route_id, db, token_data.user_id)
        db.commit()
        return response
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))

@permission_user_route_router.get("/permission_user_routes/user/{user_id}", summary="Buscar todos os usuários", response_model=List[PermissionUserRouteModel])
def get_all(user_id: int, db: Session = Depends(get_db), token_data: ReturnMiddleware = Depends(auth_token_with_permission(10))):
    try:
        service = PermissionUserRouteService()
        return service.get_by_user_id(user_id, db)
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error))