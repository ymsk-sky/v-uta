from typing import List

from sqlalchemy.orm import Session

from repositories.repository import Repository, VideoRecordDTO


class Service:
    def __init__(self, session: Session) -> None:
        """初期化

        Args:
            session (Session): セッション
        """
        self.session = session

    def get_all_video_records(self) -> List[VideoRecordDTO]:
        """全レコードを返す"""
        repository = Repository(session=self.session)
        return repository.get_all_records()
