from sqlalchemy.orm import Session

from repositories.user_repository import UserRepository
from core.security import hash_password, verify_password
from core.email_verification import generate_email_verification_token,email_verification_expiry
from repositories.email_verification_repository import EmailVerificationRepository
from api.schemas.auth import SignupResponse

class AuthService:
    @staticmethod
    def signup(db: Session, *, email:str, password: str):
        existing_user = UserRepository.get_by_email(db,email)
        if(existing_user):
            raise ValueError("User already exists")
        
        password_hash = hash_password(password)
        user = UserRepository.create(db,email=email,password_hash=password_hash)
        token = generate_email_verification_token()
        EmailVerificationRepository.create(
            db,
            token=token,
            user_id = user.id,
            expires_at=email_verification_expiry()
        )
        verification_link = f"http://localhost:8000/auth/verify-email?token={token}"

        return SignupResponse(
            id=user.id,
            email=user.email,
            verification_link=verification_link
        )
    
    @staticmethod
    def login(db:Session, *, email:str, password:str):
        user = UserRepository.get_by_email(db,email)

        if not user:
            raise ValueError("Invalid Credentials")
        
        if not verify_password(password,user.password_hash):
            raise ValueError("Invalid Credentials")
        
        return user
    
        