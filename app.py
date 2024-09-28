from src.control.mainController import MainController
from src.control.userController import UserController
from src.utils.aquisition import Aquisition

from src import app, db
import os

main = MainController()
user = UserController()
acq = Aquisition()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run( host="0.0.0.0", port=int(os.environ['PORT']), debug=int(os.environ['FLASK_DEBUG']))