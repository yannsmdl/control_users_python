import inject

from handlers.permission_user_route.copy_user_permission_user_route_handler import CopyUserPermissionUserRouteHandler
from handlers.permission_user_route.create_permission_user_route_handler import CreatePermissionUserRouteHandler
from handlers.permission_user_route.delete_permission_user_route_handler import DeletePermissionUserRouteHandler
from handlers.user.create_user_handler import CreateUserHandler
from handlers.user.delete_user_handler import DeleteUserHandler
from handlers.user.update_password_user_handler import UpdatePasswordUserHandler
from handlers.user.update_user_handler import UpdateUserHandler
from interfaces.handlers.permission_user_route.icopy_user_permission_user_route_handler import ICopyUserPermissionUserRouteHandler
from interfaces.handlers.permission_user_route.icreate_permission_user_route_handler import ICreatePermissionUserRouteHandler
from interfaces.handlers.permission_user_route.idelete_permission_user_route_handler import IDeletePermissionUserRouteHandler
from interfaces.handlers.user.icreate_user_handler import ICreateUserHandler
from interfaces.handlers.user.idelete_user_handler import IDeleteUserHandler
from interfaces.handlers.user.iupdate_password_user_handler import IUpdatePasswordUserHandler
from interfaces.handlers.user.iupdate_user_handler import IUpdateUserHandler
from interfaces.repository.ipermission_user_route_repository import IPermissionUserRouteRepository
from interfaces.repository.iroute_repository import IRouteRepository
from interfaces.repository.iuser_session_repository import IUserSessionRepository
from repositories.permission_user_route_repository import PermissionUserRouteRepository
from repositories.route_repository import RouteRepository
from repositories.user_session_repository import UserSessionRepository
from interfaces.repository.iuser_repository import IUserRepository
from repositories.user_repository import UserRepository

def injects(binder):
    ### Region Repository
    binder.bind(IUserRepository, UserRepository)
    binder.bind(IUserSessionRepository, UserSessionRepository)
    binder.bind(IRouteRepository, RouteRepository)
    binder.bind(IPermissionUserRouteRepository, PermissionUserRouteRepository)

    ### Region Handle
    binder.bind(IUpdateUserHandler, UpdateUserHandler)
    binder.bind(ICreateUserHandler, CreateUserHandler)
    binder.bind(IUpdatePasswordUserHandler, UpdatePasswordUserHandler)
    binder.bind(IDeleteUserHandler, DeleteUserHandler)

    binder.bind(IDeletePermissionUserRouteHandler, DeletePermissionUserRouteHandler)
    binder.bind(ICopyUserPermissionUserRouteHandler, CopyUserPermissionUserRouteHandler)
    binder.bind(ICreatePermissionUserRouteHandler, CreatePermissionUserRouteHandler)
    

def register_ioc():
    inject.configure(injects)