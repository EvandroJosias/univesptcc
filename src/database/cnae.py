from .. import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.inspection import inspect
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

    def to_dict(self):
        return {
            'id': self.id,
            'created': self.created.isoformat(),
            'updated': self.updated.isoformat(),            
            'cnae': self.cnae,
            'nm_cnae': self.nm_cnae
        }
    
    def get_table_structure( self ):
        # Usando a função inspect do SQLAlchemy para obter informações sobre a tabela
        print( self )
        mapper = inspect(self)
        structure = {
            'table_name': self.__tablename__,
            'columns': {}
        }

        for column in mapper.columns:
            structure['columns'][column.name] = {
                'type': str(column.type),
                'primary_key': column.primary_key,
                'nullable': column.nullable,
                'unique': column.unique,
                'default': column.default,
            }

        return structure    