import jwt
import datetime
from dotenv import load_dotenv
import os

load_dotenv("jwt.env")

SECRET_KEY = os.getenv("SECRET_KEY")
JWT_TTL_SECONDS = int(os.getenv("JWT_TTL_SECONDS", 60 * 60 * 1))

def create_token(user_id, email, is_admin):
    payload = {
        "user_id": user_id,
        "email": email,
        "admin": is_admin,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm = "HS256")
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = ["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None