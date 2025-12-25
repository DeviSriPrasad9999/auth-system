import secrets
from datetime import datetime, timezone, timedelta

from core.config import settings

REFRESH_TOKEN_EXPIRE_DAYS = 1

def generate_refresh_token() -> str:
    return secrets.token_urlsafe(64)

def refresh_token_expiry() -> datetime:
    return datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)