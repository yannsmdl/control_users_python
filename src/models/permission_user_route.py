from datetime import datetime
from sqlalchemy import DateTime, Boolean
from sqlalchemy.sql import func, false
from sqlalchemy import ForeignKey
from utils.models_base import Base
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.sqlalchemy_pydantic import sqlalchemy_to_pydantic


class PermissionUserRoute(Base):
    __tablename__ = 'permission_user_route'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
    route_id: Mapped[int] = mapped_column(ForeignKey('route.id'), primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    created_by: Mapped[int]
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    updated_by: Mapped[int] = mapped_column(nullable=True)
    deleted_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    deleted_by: Mapped[int] = mapped_column(nullable=True)

    user = relationship("User")
    route = relationship("Route")

    def update(self, db, **kwargs): 
        kwargs['updated_at'] = datetime.now()
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.add(self)

    def self_delete(self, db, **kwargs):
        kwargs['deleted_at'] = datetime.now()
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.add(self)
    