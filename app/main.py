from fastapi import FastAPI, Depends
from api.routes.auth import router
from sqlalchemy.orm import Session
from core.db import get_db
from repositories.user_repository import UserRepository
    
app = FastAPI(title="Auth Service")

app.include_router(router, prefix="/auth")