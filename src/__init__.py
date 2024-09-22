## Init file 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

logado = False

basedir = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__) ), os.pardir))

app = Flask(__name__, template_folder='./pages')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "db", os.environ['DATABASE_NAME'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['MODIFICATIONS']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

db = SQLAlchemy(app)
