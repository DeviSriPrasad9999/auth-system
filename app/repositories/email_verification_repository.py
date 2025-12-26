from sqlalchemy.orm import Session
from datetime import datetime, timezone
from uuid import UUID
from models.email_verification_token import EmailVerificationToken

class EmailVerificationRepository:

    @staticmethod
    def create(db: Session, *, token: str, user_id:UUID, expires_at: datetime):
        obj = EmailVerificationToken(
            token=token,
            user_id=user_id,
            expires_at=expires_at
        )

        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    
    @staticmethod
    def get_valid(db: Session, token: str):
        return (
            db.query(
                EmailVerificationToken
            )
            .filter(
                EmailVerificationToken.token == token,
                EmailVerificationToken.expires_at > datetime.now(timezone.utc)
            )
            .first()
        )

    @staticmethod
    def delete(db: Session, obj):
        db.delete(obj)
        db.commit()
