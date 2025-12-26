from fastapi import Request, Depends, HTTPException, status
from core.rate_limiter import rate_limit

def login_rate_limit(request: Request):
    client_ip = request.client.host if request.client else None
    if not client_ip:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests"
        )
    
    rate_limit(
        key=f"login:{client_ip}",
        limit=5,
        window_seconds=60
    )

def signup_rate_limit(request: Request):
    client_ip = request.client.host if request.client else None
    if not client_ip:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests"
        )
    
    rate_limit(
        key=f"signup:{client_ip}",
        limit=3,
        window_seconds=60
    )

def refresh_token_rate_limit(request: Request):
    client_ip = request.client.host if request.client else None
    if not client_ip:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests"
        )
    
    rate_limit(
        key=f"signup:{client_ip}",
        limit=10,
        window_seconds=60
    )