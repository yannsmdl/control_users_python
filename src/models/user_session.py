from datetime import datetime
from sqlalchemy import DateTime, Text, Boolean
from sqlalchemy.sql import func, false
from sqlalchemy import ForeignKey
from utils.models_base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.sqlalchemy_pydantic import sqlalchemy_to_pydantic


class UserSession(Base):
    __tablename__ = 'user_session'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), primary_key=True)
    token: Mapped[Text] = mapped_column(Text)
    disabled: Mapped[Boolean] = mapped_column(Boolean, server_default=false())
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    expires_in: Mapped[DateTime] = mapped_column(DateTime) 

    user = relationship("User")

    def update(self, db, **kwargs):
        kwargs['updated_at'] = datetime.now()
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.add(self)