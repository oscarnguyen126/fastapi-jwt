import time
import jwt
from decouple import config


JWT_SECRET = config("secret")
JSWT_ALGORITHM = config("algorithm")

# return token
def token_response(token: str):
    return {
        "access token" : token
    }


# create jwt string
def signJWT(userID: str):
    payload = {
        "userID" : userID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JSWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JSWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}