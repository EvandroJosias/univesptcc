from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.sql import func

from datetime import datetime

class Simples(db.Model):
    __tablename__ = 'simples'

    ## Auto generated field
    id : Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    cnpj_basico: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True )
    op_simples: Mapped[str] = mapped_column(String(200), unique=True, nullable=False )
    dt_op_simples: Mapped[int] = mapped_column(Integer, nullable=False )
    dt_exc_simples: Mapped[int] = mapped_column(Integer, nullable=False )
    op_mei: Mapped[str] = mapped_column(String(200), unique=True, nullable=False )
    dt_op_mei: Mapped[int] = mapped_column(Integer, nullable=False )
    dt_exc_mei: Mapped[int] = mapped_column(Integer, nullable=False )

    def __repr__(self):
        return '<Simples %r>' % self.cnpj_basico
