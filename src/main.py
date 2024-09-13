from flask import Flask, render_template

import os

app = Flask(__name__, template_folder='./pages')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['MODIFICATIONS']
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

@app.route('/')
def run():
    return render_template('index.html')

if __name__ == "__main__":
    app.run( host="0.0.0.0", port=int(os.environ['PORT']), debug=int(os.environ['FLASK_DEBUG']))