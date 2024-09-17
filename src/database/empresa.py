from .. import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.sql import func

from datetime import datetime

class Empresa(Base):
    __tablename__ = 'empresa'

    ## Auto generated field
    id : Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    cnpj_basico: Mapped[int] = mapped_column(primary_key=True, unique=True )
    razao_social: Mapped[str] = mapped_column(String(200), unique=True, nullable=False )
    nat_juridica: Mapped[int] = mapped_column(Integer, nullable=False )
    qual_resp: Mapped[int] = mapped_column(Integer, nullable=False )
    capital_social: Mapped[float] = mapped_column(Float, nullable=False )
    port_empresa: Mapped[int] = mapped_column(Integer, nullable=False )
    ente_fed_resp: Mapped[str] = mapped_column(String(150), nullable=False )

    def __repr__(self):
        return '<Empresa %r>' % self.cnpj_basico
