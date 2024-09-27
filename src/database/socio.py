from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.sql import func

from datetime import datetime

class Socio(db.Model):
    __tablename__ = 'socio'

    ## Auto generated field
    id : Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    cnpj_basico: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True )
    id_tipo_socio: Mapped[int] = mapped_column(Integer, nullable=False)
    nome_ou_razao_social: Mapped[str] = mapped_column(String(200), nullable=False )
    cnpj_cpf: Mapped[str] = mapped_column(String(20), nullable=False )
    qualif_socio: Mapped[int] = mapped_column(Integer, nullable=False )
    dt_entrada: Mapped[int] = mapped_column(Integer, nullable=False )
    cod_pais: Mapped[int] = mapped_column(Integer, nullable=False )
    repr_legal: Mapped[str] = mapped_column(String(200), nullable=False )
    nm_repr: Mapped[str] = mapped_column(String(200), nullable=False )
    cd_qualif_repr: Mapped[int] = mapped_column(Integer, nullable=False )
    faixa_etaria: Mapped[int] = mapped_column(Integer, nullable=False )


    def __repr__(self):
        return '<Socio %r>' % self.cnpj_basico
