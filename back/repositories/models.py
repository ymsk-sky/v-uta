from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from repositories.database import Base


class OriginalArtist(Base):
    __tablename__ = "original_artists"
    id_ = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    songs = relationship("Song", back_populates="original_artist")


class Agancy(Base):
    __tablename__ = "agencies"
    id_ = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    vtubers = relationship("Vtubers", back_populates="agency")


class Vtuber(Base):
    __tablename__ = "vtubers"
    id_ = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    agency_id = Column(Integer, ForeignKey("agencies.id_"))
    agency = relationship("Agency", back_populates="vtubers")
    video_records = relationship("VideoRecord", back_populates="vtuber")


class Song(Base):
    __tablename__ = "songs"
    id_ = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    original_artist_id = Column(Integer, ForeignKey("original_artists.id_"))
    original_artist = relationship("OriginalArtist", back_populates="songs")
    video_records = relationship("VideoRecord", back_populates="song")


class VideoRecord(Base):
    __tablename__ = "video_records"
    id_ = Column(Integer, primary_key=True, autoincrement=True)
    song_id = Column(Integer, ForeignKey("songs.id_"))
    vtuber_id = Column(Integer, ForeignKey("vtubers.id_"))
    video_type = Column(Enum("single", "utawaku", name="vide_type"), nullable=False)
    song = relationship("Song", back_populates="video_records")
    vtuber = relationship("Vtuber", back_populates="video_records")
    video_urls = relationship("VideoURL", back_populates="video_record")


class VideoURL(Base):
    __tablename__ = "video_urls"
    id_ = Column(Integer, primary_key=True, autoincrement=True)
    video_record_id = Column(Integer, ForeignKey("video_records.id_"))
    url = Column(String, nullable=False)
    uploaded_at = Column(DateTime, nullable=False)
    video_record = relationship("VideoRecord", back_populates="video_urls")
