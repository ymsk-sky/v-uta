from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from services.service import Service
from repositories.database import SessionLocal


class VideoRecordModel(BaseModel):
    song_title: str
    original_artist: str
    vtuber_name: str
    vtuber_agency: str
    video_type: str
    urls: List[str]


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


@router.get("/", response_model=List[VideoRecordModel])
def get_all_video_records(session: Session = Depends(get_session)) -> List[VideoRecordModel]:
    """全レコードを返す

    Args:
        session (Session): セッション

    """
    service = Service(session=session)
    results = service.get_all_video_records()
    return results


@router.post("/")
def add_video_record(video_record: VideoRecordModel, session: Session = Depends(get_session)):
    service = Service(session=session)
    service.add_video_record(video_record=video_record)
    return {"state": "OK"}
