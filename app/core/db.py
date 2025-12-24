from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings
from sqlalchemy import URL

url_object = URL.create(
    "postgresql+psycopg2",
    username=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.DB_HOST,
    database=settings.POSTGRES_DB,
)

engine = create_engine(url_object,pool_pre_ping=True,)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()