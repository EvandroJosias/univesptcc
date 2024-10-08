from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.sql import func

from datetime import datetime

class NatJu(db.Model):
    __tablename__ = 'natju'

    ## Auto generated field
    id : Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    cd_nat_juridica: Mapped[int] = mapped_column(primary_key=True, unique=True )
    nat_juridica: Mapped[str] = mapped_column(String(200), unique=True, nullable=False )

    def __repr__(self):
        return '<NatJu %r>' % self.cd_nat_juridica
