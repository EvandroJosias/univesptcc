from .. import db
from datetime import datetime
from sqlalchemy import inspect


class User(db.Model):
    __tablename__ = 'users'

    ## Auto generated field
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated = db.Column(db.DateTime(timezone=True), default=datetime.now)

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        return '<User %r>' % self.username
