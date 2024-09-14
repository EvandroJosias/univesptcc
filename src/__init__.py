## Init file 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

import os

logado = False

app = Flask(__name__, template_folder='./pages')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['MODIFICATIONS']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

db = SQLAlchemy()
db.init_app(app)

engine = create_engine(os.environ['DATABASE_URI'], echo=True)

class Base(DeclarativeBase):
    pass
