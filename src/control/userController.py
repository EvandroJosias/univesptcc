from flask import request, jsonify
#from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

from src.database.user import User 
from src.utils.authenticate import generate_jwt, generate_password_hash
from src import app, db


import os


class UserController():
    def __init__(self) -> None:        
        self.setEndpoints()

    def create(self):
        data = request.get_json()
        passwd = generate_password_hash(data['password'])
        new_user = User(username=data['username'], password=passwd, email=data['email']) 
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201

    def read(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()        
        if user:
            return jsonify(user.to_dict())
        else:
            return jsonify({'error': 'User not found'}), 404

    def readall(self):
        users = User.query.all()  # Consulta todos os usuários
        return jsonify([user.to_dict() for user in users])  # Retorna todos os usuários como uma lista de dicionários
            
    def update(self, user_id):
        data = request.get_json()
        user = User.query.get(user_id)
        if user:
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            if 'password' in data:
                passwd = generate_password_hash(data['password'])
                user.password = passwd
            db.session.commit()
            return jsonify({'message': 'User updated successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    def delete(self, user_id):
        data = request.get_json()
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404     

    def userlogin(self):
        data = request.get_json()
        passwd = generate_password_hash(data['password'])      
        print("dentro do userLogin")
        user = User.query.filter_by( username=data['username'], password=passwd ).first()
        if user:
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=int(os.environ['TIME_LIFE'])),
                'iat': datetime.utcnow(),
                "sub": user.id
            }
            token = generate_jwt(payload)
            return jsonify({"token": token}),  200
        return jsonify({"message":"Invalid username or password"}), 401
    
    def setEndpoints(self) -> None:
        app.add_url_rule('/api/userregister', view_func=self.create, methods=['POST'])
        app.add_url_rule('/api/userbyname', view_func=self.read, methods=['GET'])
        app.add_url_rule('/api/allusers', view_func=self.readall, methods=['GET'])
        app.add_url_rule('/api/user/<int:user_id>', view_func=self.update, methods=['PUT'])
        app.add_url_rule('/api/user/<int:user_id>', view_func=self.delete, methods=['DELETE'])
        app.add_url_rule('/api/login', view_func=self.userlogin, methods=['POST'])        
