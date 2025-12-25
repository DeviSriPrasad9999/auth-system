from sqlalchemy.orm import Session
from models.user import User
from uuid import UUID

class UserRepository:
    @staticmethod
    def get_by_email(db:Session,email:str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_by_id(db: Session, id: UUID) -> User | None:
        return db.query(User).filter(User.id == id).first()
    
    @staticmethod
    def create(
        db: Session,
        *,
        email: str,
        password_hash: str,
    ) -> User:
        user = User(
            email=email,
            password_hash=password_hash
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user