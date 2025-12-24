from fastapi import FastAPI
from api.routes.auth import router
from core.db import get_db, engine
from models.base import Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Base=============>",Base)
    print("TABLES KNOWN TO SQLALCHEMY:", Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.clear()
    
app = FastAPI(title="Auth Service",lifespan=lifespan)


app.include_router(router, prefix="/auth")