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
        video_records = self.session.query(VideoRecord).all()
        results = []
        for video_record in video_records:
            song = self.session.query(Song).filter_by(id_=video_record.song_id).first()
            original_artist = self.session.query(OriginalArtist).filter_by(id_=song.original_artist_id).first()
            vtuber = self.session.query(Vtuber).filter_by(id_=video_record.vtuber_id).first()
            agency = self.session.query(Agency).filter_by(id_=vtuber.agency_id).first()
            video_urls = self.session.query(VideoURL).filter_by(video_record_id=video_record.id_).all()
            results.append(
                VideoRecordDTO(
                    song_title=song.title,
                    original_artist=original_artist.name,
                    vtuber_name=vtuber.name,
                    vtuber_agency=agency.name,
                    video_type=video_record.video_type,
                    urls=[video_url.url for video_url in video_urls],
                )
            )
        return results

    def add_video_record(self, video_record: VideoRecordDTO):
        """登録処理"""
        original_artist = self.session.query(OriginalArtist).filter_by(name=video_record.original_artist).first()
        if not original_artist:
            original_artist = OriginalArtist(name=video_record.original_artist)
            self.session.add(original_artist)
            self.session.commit()
            self.session.refresh(original_artist)

        song = self.session.query(Song).filter_by(title=video_record.song_title).first()
        if not song:
            song = Song(title=video_record.song_title, original_artist_id=original_artist.id_)
            self.session.add(song)
            self.session.commit()
            self.session.refresh(song)

        agency = self.session.query(Agency).filter_by(name=video_record.vtuber_agency).first()
        if not agency:
            agency = Agency(name=video_record.vtuber_agency)
            self.session.add(agency)
            self.session.commit()
            self.session.refresh(agency)

        vtuber = self.session.query(Vtuber).filter_by(name=video_record.vtuber_name).first()
        if not vtuber:
            vtuber = Vtuber(name=video_record.vtuber_name, agency_id=agency.id_)
            self.session.add(vtuber)
            self.session.commit()
            self.session.refresh(vtuber)

        _video_record = self.session.query(VideoRecord).filter_by(song_id=song.id_, vtuber_id=vtuber.id_).first()
        if _video_record:
            # 既に存在する場合そのVideoRecordのIDを使用
            record_id = _video_record.id_
        else:
            # 新規で作成
            video_record_db = VideoRecord(
                song_id=song.id_,
                vtuber_id=vtuber.id_,
                video_type=video_record.video_type,
            )
            self.session.add(video_record_db)
            self.session.commit()
            self.session.refresh(video_record_db)
            record_id = video_record_db.id_

        for url in video_record.urls:
            video_url = VideoURL(video_record_id=record_id, url=url)
            self.session.add(video_url)
        self.session.commit()
