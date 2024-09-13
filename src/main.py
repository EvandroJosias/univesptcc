from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__, template_folder='./pages')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['MODIFICATIONS']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

db = SQLAlchemy( app )

@app.route('/teste')
def teste():
    return render_template('index.html')


@app.route('/')
def run():
    return "{\"message\":\"Hey there python\"}"


if __name__ == "__main__":
    app.run( host="0.0.0.0", port=int(os.environ['PORT']), debug=int(os.environ['FLASK_DEBUG']))