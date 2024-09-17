from flask import render_template, redirect, request
from src import app, logado
from src.database.user import User
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

import logging


class MainController():

    def __init__(self) -> None:
        self.setEndpoints()

    def main(self):
        if logado:
            return render_template('index.html')
        else:
            return redirect('login')

    def login(self):
        if request.method == 'POST':
            usuario = request.form['usuario']
            senha = request.form['password']
            logging.warning(usuario)
            logging.warning(senha)
            #resp = User.query.filter_by(username="'"+usuario+"'", password="'"+password+"'")
            resp = User.query.filter_by(username=usuario, password=senha)
            logging.warning(resp)            
        return render_template('login.html')

    def setEndpoints(self) -> None:
        app.add_url_rule('/', view_func=self.main, methods=['GET'])
        app.add_url_rule('/login', view_func=self.login, methods=['GET', 'POST' ])
