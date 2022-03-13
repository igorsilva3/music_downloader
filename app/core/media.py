# Media
# Author, Title, Date, Views, Description, Streams, Rating, thubnail, uri

import datetime

from pytube import Stream, YouTube


class Media:
    author: str = ''
    title: str = ''
    date_published: datetime = None
    description: str = ''
    streams: list(Stream) = []
    rating: float = 0.0
    views: int = 0
    thumbnail: str = ''
    uri: str = ''
    
    __youtube: YouTube
    
    def __init__(self, url: str):
        self.__youtube = YouTube(url)
        self.__get_media_info()

    def __get_media_info(self) -> None:
        self.author = self.__youtube.author
        self.title = self.__youtube.title
        self.date_published = self.__youtube.publish_date
        self.thumbnail = self.__youtube.thumbnail_url
        self.rating = self.__youtube.rating
        self.streams = self.__youtube.streams
        self.views = self.__youtube.views
        self.description = self.__youtube.description
        self.uri = self.__youtube.watch_url
