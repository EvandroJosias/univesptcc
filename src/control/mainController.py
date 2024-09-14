from flask import render_template, redirect
from src import app, logado


class MainController():

    def __init__(self) -> None:
        self.setEndpoints()

    def main(self):
        if logado:
            return render_template('index.html')
        else:
            return redirect('login')
        
    def login(self):
        return render_template('login.html')

    def setEndpoints(self) -> None:
        app.add_url_rule('/', view_func=self.main, methods=['GET'])
        app.add_url_rule('/login', view_func=self.login, methods=['GET','POST'])
