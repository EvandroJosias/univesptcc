from flask import render_template, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from src import app, logado
from src.database.user import User

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
       
            # Busca o usuário pela username
            user = User.query.filter_by(username=usuario).first()
        
            # Verifica se o usuário existe e a senha está correta
            if user and check_password_hash(user.password, senha):
                # Senha correta, prossiga com o login
                # (Adicione aqui sua lógica de autenticação)
                return "Login bem-sucedido!"
            else:
                return "Usuário ou senha incorretos."
        return render_template('login.html')

    def setEndpoints(self) -> None:
        app.add_url_rule('/', view_func=self.main, methods=['GET'])
        app.add_url_rule('/login', view_func=self.login, methods=['GET', 'POST' ])
