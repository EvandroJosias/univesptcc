from flask import render_template, redirect, request, session, make_response
from src.utils.authenticate import check_password_hash
from src.database.user import User
from src import app

import os
import json
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
        app.add_url_rule('/busca', view_func=self.chat, methods=['POST'])

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
        # ler o arquivo json com os dados
        base_dir = os.path.dirname(os.path.abspath(__file__))
        app_path = os.path.dirname( base_dir )

        pesquisado = request.form['SOCIO']
        if pesquisado == "ANDRE AUGUSTO FERREIRA FONTES":
            arquivo_json = app_path+"/static/DF1.json" 
        elif pesquisado == "ALEXANDRE TADEU DA COSTA":
            arquivo_json = app_path+"/static/DF2.json" 
        elif pesquisado == "ARTHUR QUEIROGA BANDEIRA DE AGUIAR":
            arquivo_json = app_path+"/static/DF3.json" 
        else:
            arquivo_json = app_path+"/static/DF0.json" 
        
        try:
            with open(arquivo_json, 'r', encoding='utf-8') as f:
                dados = json.load(f)
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON.")
        except FileNotFoundError:
            print(f"O arquivo {arquivo_json} não foi encontrado.")


        # Criar o grafo societário
        G = nx.DiGraph()

        for entidade in dados:
            socio   = entidade["NOME_OU_RAZAO_SOCIAL"]
            empresa = "CNPJ "+str(entidade["CNPJ_BASICO"])+"\n"+entidade["RAZAO_SOCIAL"]
            
            # Adicionando nós (empresas)
            if not G.has_node( socio ):  # Verifica se o nó já existe
               G.add_node( socio, tipo='socio' )
            if not G.has_node( empresa ):  # Verifica se o nó já existe
               G.add_node( empresa, tipo='empresa' )   

            # Adicionando arestas (relações societárias)
            G.add_edge( socio, empresa)  

        # Gerar a cor dos nós com base no atributo 'tipo'
        node_colors = []
        for node in G.nodes():
            if G.nodes[node]['tipo'] == 'socio':
                node_colors.append('lightgreen')  # Cor para os sócios
            else:
                node_colors.append('lightblue')  # Cor para as empresas

        # Gerar e salvar a imagem do grafo
        image_path = os.path.join(app.static_folder, 'graph.png')
        plt.figure(figsize=(8, 8))
        nx.draw(G, with_labels=True, node_color=node_colors, node_size=2000, font_size=6, font_weight='bold', edge_color='gray')
        plt.savefig(image_path)
        plt.close()

        # Renderizar o template com o caminho da imagem
        return render_template('busca.html', graph_image='graph.png',  dados=dados )
