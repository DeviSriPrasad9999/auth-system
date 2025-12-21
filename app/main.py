from fastapi import FastAPI
from api.routes.auth import router

app = FastAPI(title="Auth Service")

app.include_router(router, prefix="/auth")