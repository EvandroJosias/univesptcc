from src.control.mainController import MainController

from flask import render_template

from src import app, Base, engine
import os

main = MainController()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run( host="0.0.0.0", port=int(os.environ['PORT']), debug=int(os.environ['FLASK_DEBUG']))