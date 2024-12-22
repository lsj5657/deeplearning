import jwt
import time
from config import AK, SK

def encode_jwt_token(ak=AK, sk=SK):
    payload = {
        "iss": ak,
        "exp": int(time.time()) + 1800,  # 현재 시간 + 30분
        "nbf": int(time.time()) - 5      # 현재 시간 - 5초
    }
    token = jwt.encode(payload, sk, algorithm="HS256")
    return token
