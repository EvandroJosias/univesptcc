from .. import Base, engine
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.sql import func

from datetime import datetime
from sqlalchemy import inspect


class User(Base):
    __tablename__ = 'users'

    ## Auto generated field
    id : Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    username: Mapped[str] = mapped_column(String(30), unique=True, nullable=False )
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False )
    password: Mapped[str] = mapped_column(String(120), unique=True, nullable=False )

    def __repr__(self):
        return '<User %r>' % self.username
