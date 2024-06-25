from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from repositories.database import SessionLocal


router = APIRouter()


def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()


@router.get("/")
def home(session: Session = Depends(get_session)):
    return {"test": "OK"}
