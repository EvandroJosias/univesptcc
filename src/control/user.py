from flask import request, jsonify
from database.user import User 

from authentication import *

from src import app
import datetime
import logging

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    logging.warning( data )
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return "User created successfully", 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=int(os.environ['TIME_LIFE'])),
            'iat': datetime.datetime.utcnow(),
            "sub": user.id
        }
        token = generate_jwt(payload)
        return jsonify({"token": token})
    return "Invalid username or password", 401

@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    authorization = request.headers.get('Authorization')
    token = authorization.split(' ')[1]
    if not token:
        return "Token is missing", 422
    payload = verify_jwt(token)
    if not payload:
        return "Token is invalid", 422
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'username': user.username, 'email': user.email})

@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    authorization = request.headers.get('Authorization')
    token = authorization.split(' ')[1]
    if not token:
        return "Token is missing", 422
    payload = verify_jwt(token)
    if not payload:
        return "Token is invalid", 422
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "Usuário não encontrado"}), 404
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({"message": "Usuário deletado com sucesso"})

@app.route("/users", methods=["GET"])
def list_users():
    authorization = request.headers.get('Authorization')
    token = authorization.split(' ')[1]
    if not token:
        return "Token is missing", 422
    payload = verify_jwt(token)
    if not payload:
        return "Token is invalid", 422
    
    users = User.query.all()
    if not users:
        return jsonify({"message": "Não há usuários cadastrados"}), 404
    
 
    result = [user.username for user in users]
    
    return jsonify({"users": result})