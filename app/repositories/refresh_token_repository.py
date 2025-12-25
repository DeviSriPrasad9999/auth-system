from sqlalchemy.orm import Session
from datetime import datetime, timezone
from uuid import UUID
from models.refresh_token import RefreshToken

class RefreshTokenRepository:
    @staticmethod
    def create(db: Session, *, token: str, user_id:UUID, expires_at:datetime):
        rt = RefreshToken(
            token=token,
            user_id=user_id,
            expires_at=expires_at
        )
        db.add(rt)
        db.commit()
        db.refresh(rt)
        return rt
    
    @staticmethod
    def get_valid(db: Session, token: str):
        return (
            db.query(RefreshToken)
            .filter(
                RefreshToken.token == token,
                RefreshToken.revoked.is_(False),
                RefreshToken.expires_at > datetime.now(timezone.utc)
            )
            .first()
        )
    
    @staticmethod
    def revoke(db: Session, token: str):
        rt = db.query(RefreshToken).filter_by(token=token).first()
        if rt:
            rt.revoked = True
            db.commit()
        
