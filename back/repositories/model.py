from sqlalchemy import Column, DateTime, Integer, String

from repositories.database import Base


class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, nullable=False)
    song_name = Column(String, nullable=False)
    singer_name = Column(String, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
