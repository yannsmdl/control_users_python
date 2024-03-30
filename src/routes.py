from fastapi import APIRouter
from controllers.user_controller import user_router
from controllers.login_controller import login_router
from controllers.permission_user_route_controller import permission_user_route_router

router = APIRouter()

router.include_router(user_router, tags=["User"])
router.include_router(login_router, tags=["Login"])
router.include_router(permission_user_route_router, tags=["Permission User Routes"])