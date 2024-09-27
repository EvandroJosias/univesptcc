from src.database.cnae import Cnae
from src.database.empresa import Empresa
from src.database.estabele import Estabele
from src.database.motivosit import MotivoSit
from src.database.municipio import Municipio
from src.database.natju import NatJu
from src.database.pais import Pais
from src.database.quals import Quals
from src.database.simples import Simples
from src.database.socio import Socio

from src.control.mainController import MainController
from src.control.userController import UserController

from src import app, db
import os

main = MainController()
user = UserController()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run( host="0.0.0.0", port=int(os.environ['PORT']), debug=int(os.environ['FLASK_DEBUG']))