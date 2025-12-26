import secrets
from datetime import datetime, timedelta, timezone

EMAIL_VERIFY_EXPIRE_HOURS = 24

def generate_email_verification_token() -> str:
    return secrets.token_urlsafe(48)

def email_verification_expiry() -> datetime:
    return datetime.now(timezone.utc) + timedelta(hours=EMAIL_VERIFY_EXPIRE_HOURS)