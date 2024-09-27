from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.sql import func

from datetime import datetime

class Estabele(db.Model):
    __tablename__ = 'estabele'

    ## Auto generated field
    id : Mapped[int] = mapped_column(primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    cnpj_basico: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True )
    cnpj_ordem: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True )
    cnpj_dv: Mapped[int] = mapped_column(Integer, nullable=False)
    cd_matriz_filial: Mapped[int] = mapped_column(Integer, nullable=False)  
    nm_fantasia: Mapped[str] = mapped_column(String(200), nullable=False )
    cd_sit_cadastro: Mapped[int] = mapped_column(Integer, nullable=False)
    dt_sit_cadastro: Mapped[int] = mapped_column(Integer, nullable=False)
    motivo_sit_cadastro: Mapped[int] = mapped_column(Integer, nullable=False)
    nm_cidade_ext: Mapped[str] = mapped_column(String(200))
    cd_pais: Mapped[int] = mapped_column(Integer)
    dt_ini: Mapped[int] = mapped_column(Integer, nullable=False)
    cnae_principal: Mapped[str] = mapped_column(String(200), nullable=False)
    cnae_secundario: Mapped[str] = mapped_column(String(200))
    tip_logradouro: Mapped[str] = mapped_column(String(200))
    logradouro: Mapped[str] = mapped_column(String(200))
    numero: Mapped[str] = mapped_column(String(200))
    complemento: Mapped[str] = mapped_column(String(200))
    bairro: Mapped[str] = mapped_column(String(200))
    cep: Mapped[str] = mapped_column(String(200))
    uf: Mapped[str] = mapped_column(String(200),nullable=False)
    municipio: Mapped[int] = mapped_column(Integer,nullable=False)
    ddd_1: Mapped[str] = mapped_column(String(200))
    tel_1: Mapped[str] = mapped_column(String(200))
    ddd_2: Mapped[str] = mapped_column(String(200))
    tel_2: Mapped[str] = mapped_column(String(200))
    ddd_fax: Mapped[str] = mapped_column(String(200))
    fax: Mapped[str] = mapped_column(String(200))
    email: Mapped[str] = mapped_column(String(200))
    sit_esp: Mapped[str] = mapped_column(String(200))
    dt_sit_esp: Mapped[int] = mapped_column(Integer)


    def __repr__(self):
        return '<Estabele %r>' % self.cnpj_basico
