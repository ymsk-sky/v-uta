from typing import List

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
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


class RecordFilterModel(BaseModel):
    song_title: str | None
    original_artist: str | None
    vtuber_name: str | None
    vtuber_agency: str | None
    video_type: str | None


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

@router.get("/records", response_model=List[VideoRecordModel])
def get_filtered_records(record_filter: RecordFilterModel, session: Session = Depends(get_session)) -> List[VideoRecordModel]:
    """条件に合うレコードを返す

    Args:
        session (Session): セッション
    """
    service = Service(session=session)
    results = service.get_filtered_video_records(record_filter)
    return results

@router.post("/")
def add_video_record(video_record: VideoRecordModel, session: Session = Depends(get_session)) -> JSONResponse:
    """レコード登録

    Args:
        video_record (VideoRecordModel): 登録するレコード
        session (Session): セッション
    """
    service = Service(session=session)
    service.add_video_record(video_record=video_record)
    return jsonable_encoder({"state": "OK"})
