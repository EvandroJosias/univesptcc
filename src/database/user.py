from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.sql import func

from datetime import datetime


class User(db.Model):
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

    def to_dict(self):
        return {
            'id': self.id,
            'created': self.created.isoformat(),
            'updated': self.updated.isoformat(),            
            'username': self.username,
            'email': self.email,
            'password': self.password
        }