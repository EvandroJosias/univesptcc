from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.sql import func

from datetime import datetime

class Cnae(db.Model):
    __tablename__ = 'cnae'

    ## Auto generated field
    id : Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    cnae: Mapped[int] = mapped_column(primary_key=True, unique=True )
    nm_cnae: Mapped[str] = mapped_column(String(200), unique=True, nullable=False )

    def __repr__(self):
        return '<Cnae %r>' % self.cnae
