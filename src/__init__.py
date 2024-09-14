## Init file 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

import os

logado = False

app = Flask(__name__, template_folder='./pages')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['MODIFICATIONS']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

db = SQLAlchemy(app)
db.session.commit()
#migrate = Migrate()

#db.init_app(app)
#migrate.init_app(app, db)
