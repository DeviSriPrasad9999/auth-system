from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class SignupRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class SignupResponse(BaseModel):
    id: UUID
    email: EmailStr
    
class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class LoginResponse(BaseModel):
    access_token: str    
    refresh_token: str

class RefreshTokenRequest(BaseModel):
    refresh_token: str