import json
# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

from helper.youtube_api_manual import printj, youtube


class Channel:
    """Класс для ютуб-канала"""
    api_key = 'AIzaSyAf6dv819F8knMNnLsYzLb38j3l3GROa5c'
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics')
        print(channel)
