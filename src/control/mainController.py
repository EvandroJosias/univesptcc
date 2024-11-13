from flask import render_template, redirect, request, session, make_response
from src.utils.authenticate import check_password_hash
from src.database.user import User
from src import app

import os
import networkx as nx
import matplotlib.pyplot as plt

import requests

class MainController():

    def __init__(self) -> None:
        self.setEndpoints()

    def setEndpoints(self) -> None:
        app.add_url_rule('/', view_func=self.main, methods=['GET','POST'])
        app.add_url_rule('/login', view_func=self.login, methods=['GET','POST'])
        app.add_url_rule('/busca', view_func=self.busca, methods=['GET'])
        app.add_url_rule('/sobre', view_func=self.sobre, methods=['GET'])
        app.add_url_rule('/ajuda', view_func=self.ajuda, methods=['GET'])
        app.add_url_rule('/chat', view_func=self.chat, methods=['GET'])

    def main(self):
        if request.method == 'POST':
            # print("post do main")
            # session['usuario'] = session.get('usuario','Visitante')
            # response = make_response( render_template('index.html', usuario=session['usuario']))
            # response.set_cookie( 'usuario', session['usuario'])
            # return response
            print("post do login")
            usuario = request.form['usuario']
            senha = request.form['password']
            base_url = request.url_root + 'api/login'
            retapi = requests.post(base_url, json={'username':usuario,'password':senha})
            if retapi.status_code == 200:
                token = retapi.json().get('token')
                session['usuario'] = usuario
                session['token'] = token                
                response = make_response( render_template('index.html', usuario=session['usuario'], token=session['token']))
                response.set_cookie( 'token', session['token'] )
                response.set_cookie( 'usuario', session['usuario'])
                return response 
                            
            # Busca o usuário pela username
            user = User.query.filter_by(username=usuario).first()
        
            # Verifica se o usuário existe e a senha está correta
            if user and check_password_hash(user.password, senha):
                print("entrou aqui")
                session['usuario'] = usuario
                session['token'] = token                
                response = make_response( render_template('index.html', usuario=session['usuario'], token=session['token']))
                response.set_cookie( 'token', session['token'] )
                response.set_cookie( 'usuario', session['usuario'])
                return response                
            else:
                return "Usuário ou senha incorretos."
        else:
            print("else do main")
            usuario = session.get('usuario','Visitante')
            cookie_usuario = request.cookies.get('usuario','Sem cookie')            
            #return render_template( 'login.html', usuario=usuario, cookie_usuario=cookie_usuario )
            return render_template( 'index.html' )

    def login(self):
        if request.method == 'POST':
            print("post do login funcao login")
            usuario = request.form['usuario']
            senha = request.form['password']
       
            # Busca o usuário pela username
            user = User.query.filter_by(username=usuario).first()
        
            # Verifica se o usuário existe e a senha está correta
            if user and check_password_hash(user.password, senha):
                print("entrou aqui")
                session['usuario'] = usuario
                response = make_response( render_template('index.html', usuario=session['usuario']))
                response.set_cookie( 'usuario', session['usuario'])
                return render_template('busca.html')
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')

    def busca(self):
        return render_template('busca.html')

    def ajuda(self):
        return render_template('ajuda.html')

    def sobre(self):
        return render_template('sobre.html')
    
    def chat(self):
        # Criar o grafo societário
        G = nx.DiGraph()

        # Adicionando nós (empresas)
        G.add_node("Empresa A")
        G.add_node("Empresa B")
        G.add_node("Empresa C")
        G.add_node("Empresa D")

        # Adicionando arestas (relações societárias)
        G.add_edge("Empresa A", "Empresa B")  # Empresa A possui participação na Empresa B
        G.add_edge("Empresa A", "Empresa C")  # Empresa A possui participação na Empresa C
        G.add_edge("Empresa B", "Empresa D")  # Empresa B possui participação na Empresa D

        # Gerar e salvar a imagem do grafo
        image_path = os.path.join(app.static_folder, 'graph.png')
        plt.figure(figsize=(8, 8))
        nx.draw(G, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')
        plt.savefig(image_path)
        plt.close()

        # Renderizar o template com o caminho da imagem
        return render_template('chat.html', graph_image='graph.png')
