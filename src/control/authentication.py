import jose
import jwt
import os

def generate_jwt(payload):
    token = jwt.encode(payload, os.environ['SECRET_KEY'] , algorithm=os.environ['ALGORITHM'] )
    return token

def verify_jwt(token):
    try:
        header, payload, signature = jose.decode(token, os.environ['SECRET_KEY'], algorithms=[os.environ['ALGORITHM']])
        return payload
    except jose.exceptions.JWTError as e:
        return None