from .. import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.sql import func

from datetime import datetime

class MotivoSit(Base):
    __tablename__ = 'motivosit'

    ## Auto generated field
    id : Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    cd_motivo_sit_cadastro: Mapped[int] = mapped_column(primary_key=True, unique=True )
    motivo_sit_cadastro: Mapped[str] = mapped_column(String(200), unique=True, nullable=False )

    def __repr__(self):
        return '<MotivoSit %r>' % self.cd_motivo_sit_cadastro
