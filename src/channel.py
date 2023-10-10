import os

from googleapiclient.discovery import build

# api_key: str = os.getenv('YT_API_KEY')
# print(os.getenv('YT_API_KEY'))
#
class Channel:
    """Класс для ютуб-канала"""
    api_key = 'AIzaSyAf6dv819F8knMNnLsYzLb38j3l3GROa5c'
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(channel)
