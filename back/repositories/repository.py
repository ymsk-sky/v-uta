from typing import List

from sqlalchemy.orm import Session


class Repository:
    def __init__(self, session: Session) -> None:
        """初期化

        Args:
            session(Session): セッション
        """
        self.session = session

    def create_item(self) -> None:
        pass

    def delete_item(self) -> None:
        pass

    def get_all_items(self) -> List:
        pass

    def get_one_item(self) -> None:
        pass
