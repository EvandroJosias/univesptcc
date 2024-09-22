import jwt
import os

def generate_jwt(payload):
    token = jwt.encode(payload, os.environ['SECRET_KEY'] , algorithm=os.environ['ALGORITHM'] )
    return token

def verify_jwt(token):
    is_decoded = False
    try:
        user_id = jwt.decode(token, os.environ['SECRET_KEY'], algorithms=[os.environ['ALGORITHM']])
        if user_id:
            is_decoded = True
        return is_decoded
    except:
        return is_decoded    
