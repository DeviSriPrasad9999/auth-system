from sqlalchemy.orm import Session

from repositories.user_repository import UserRepository
from core.security import hash_password, verify_password

class AuthService:
    @staticmethod
    def signup(db: Session, *, email:str, password: str):
        existing_user = UserRepository.get_by_email(db,email)
        if(existing_user):
            raise ValueError("User already exists")
        
        password_hash = hash_password(password)
        user = UserRepository.create(db,email=email,password_hash=password_hash)
        return user
    
    @staticmethod
    def login(db:Session, *, email:str, password:str):
        user = UserRepository.get_by_email(db,email)

        if not user:
            raise ValueError("Invalid Credentials")
        
        if not verify_password(password,user.password_hash):
            raise ValueError("Invalid Credentials")
        
        return user
    
        