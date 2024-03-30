from datetime import datetime
from sqlalchemy.sql import func
from utils.models_base import Base
from sqlalchemy import DateTime, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from utils.sqlalchemy_pydantic import sqlalchemy_to_pydantic


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    birth_date: Mapped[Date] = mapped_column(Date)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    created_by: Mapped[int]
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    updated_by: Mapped[int] = mapped_column(nullable=True)
    deleted_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    deleted_by: Mapped[int] = mapped_column(nullable=True)

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

