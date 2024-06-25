from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import QueuePool


DATABASE_URL = "sqlite:///./vuta.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=QueuePool, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
