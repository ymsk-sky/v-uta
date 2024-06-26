from typing import List

from sqlalchemy.orm import Session

from repositories.models import Agency, OriginalArtist, Song, VideoRecord, VideoURL, Vtuber


class VideoRecordDTO:
    """DTO: データ転送オブジェクト"""
    def __init__(
        self,
        song_title: str,
        original_artist: str,
        vtuber_name: str,
        vtuber_agency: str,
        video_type: str,
        urls: List[str],
    ) -> None:
        self.song_title = song_title
        self.original_artist = original_artist
        self.vtuber_name = vtuber_name
        self.vtuber_agency = vtuber_agency
        self.video_type = video_type
        self.urls = urls


class Repository:
    def __init__(self, session: Session) -> None:
        """初期化

        Args:
            session (Session): セッション
        """
        self.session = session

    def get_all_records(self) -> List[VideoRecordDTO]:
        """全レコードを返す"""
        # video_records = self.session.query(VideoRecord).all()
        results = []
        # for video_record in video_records:
        #     song = self.session.query(Song).filter_by(id_=video_record.song_id).first()
        #     original_artist = self.session.query(OriginalArtist).filter_by(id_=song.original_artist_id).first()
        #     vtuber = self.session.query(Vtuber).filter_by(id_=video_record.vtuber_id).first()
        #     agency = self.session.query(Agency).filter_by(id_=vtuber.agency_id).first()
        #     video_urls = self.session.query(VideoURL).filter_by(video_record_id=video_record.id_).all()
        #     results.append(
        #         VideoRecordDTO(
        #             song_title=song.title,
        #             original_artist=original_artist.name,
        #             vtuber_name=vtuber.name,
        #             vtuber_agency=agency.name,
        #             video_type=video_record.video_type,
        #             urls=video_urls,
        #         )
        #     )
        results.append(
            VideoRecordDTO("song", "artist", "vtuber", "agency", "utawaku", ["url0"])
        )
        return results
