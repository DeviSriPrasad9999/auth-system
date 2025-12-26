import time
from fastapi import HTTPException, status
from core.redis import redis_client
from typing import cast

def rate_limit(
    *,
    key: str,
    limit: int,
    window_seconds: int
):
    """
    Fixed window rate limiting
    """
    current_window = int(time.time() // window_seconds) 
    redis_key = f"rate_limit:{key}:{current_window}"

    current_count = cast(int,redis_client.incr(redis_key))

    if current_count == 1:
        redis_client.expire(redis_key,window_seconds)

    if current_count > limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests, slow down"
        )
    
