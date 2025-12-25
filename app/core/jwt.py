from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from uuid import UUID

from .config import settings

def create_access_token(*, user_id: UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "exp": expire,
        "type": "access"
    }

    token = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        settings.JWT_ALGORITHM
    )

    return token

def decode_access_token(token: str) -> UUID:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            settings.JWT_ALGORITHM
        )

        if payload.get("type") != "access":
            raise ValueError("Invalid token type")
        
        user_id = payload.get("sub")
        if not user_id:
            raise ValueError("Missing subject")
        
        return UUID(user_id)
    except (JWTError, ValueError):
        raise