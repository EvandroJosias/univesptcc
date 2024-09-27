from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.sql import func

from datetime import datetime

class Pais(db.Model):
    __tablename__ = 'pais'

    ## Auto generated field
    id : Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    cod_pais: Mapped[int] = mapped_column(primary_key=True, unique=True )
    pais: Mapped[str] = mapped_column(String(150), unique=True, nullable=False )

    def __repr__(self):
        return '<Pais %r>' % self.cod_pais
