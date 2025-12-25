from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from core.db import get_db
from models.user import User
from api.schemas.auth import SignupRequest, SignupResponse, LoginRequest, LoginResponse,RefreshTokenRequest
from services.auth_service import AuthService
from core.jwt import create_access_token
from core.refresh_token import generate_refresh_token, refresh_token_expiry
from repositories.refresh_token_repository import RefreshTokenRepository
from api.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/login",response_model=LoginResponse,status_code=status.HTTP_200_OK)
def login(payload:LoginRequest, db: Session = Depends(get_db)):
    try:
        user = AuthService.login(db,email=payload.email,password=payload.password)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc)
        )
    
    access_token = create_access_token(user_id=user.id)
    refresh_token = generate_refresh_token()
    RefreshTokenRepository.create(
        db,
        token=refresh_token,
        user_id=user.id,
        expires_at=refresh_token_expiry()
    )
    return LoginResponse(access_token=access_token,refresh_token=refresh_token)

@router.post("/signup",response_model=SignupResponse,status_code=status.HTTP_201_CREATED)
def signup(payload: SignupRequest, db: Session = Depends(get_db)):
    try:
        user = AuthService.signup(db,email=payload.email,password=payload.password)
    
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail= str(exc),
        )
    
    return SignupResponse(
        id=user.id,
        email=user.email 
    )
    
@router.post("/refresh")
def refresh_token(
    payload: RefreshTokenRequest,
    db: Session = Depends(get_db)
):
    rt = RefreshTokenRepository.get_valid(db,payload.refresh_token)
    if not rt:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token"
        )
    
    RefreshTokenRepository.revoke(db, payload.refresh_token)

    new_refresh_token = generate_refresh_token()
    RefreshTokenRepository.create(
        db,
        token=new_refresh_token,
        user_id=rt.user_id,
        expires_at=refresh_token_expiry()
    )
    new_access_token = create_access_token(user_id=rt.user_id)

    return LoginResponse(
        access_token=new_access_token,
        refresh_token=new_refresh_token
    )

@router.post("/logout")
def logout(
    payload: RefreshTokenRequest,
    db: Session = Depends(get_db)
):
    RefreshTokenRepository.revoke(db,payload.refresh_token)
    return { "detail": "Logged Out" }

@router.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email
    }
