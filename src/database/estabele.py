from .. import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.sql import func

from datetime import datetime

class Estabele(Base):
    __tablename__ = 'estabele'

    ## Auto generated field
    id : Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    cnpj_basico: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True )
    cnpj_ordem: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True )
    nm_cnae: Mapped[str] = mapped_column(String(200), unique=True, nullable=False )

    def __repr__(self):
        return '<Estabele %r>' % self.cnpj_basico
