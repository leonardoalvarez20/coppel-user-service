from datetime import datetime, timedelta

from jose import jwt

from app.config.settings import settings

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440


def create_access_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.secret_key, algorithm=ALGORITHM
    )
    return encoded_jwt


def decode_token(token: str):
    payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
    return payload.get("sub")
