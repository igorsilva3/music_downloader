from pathlib import Path

from .core.downloader import Downloader
from .core.media import Media


class App: 
  def download_music(self, url: str) -> Path:
    media = Media(url)
    downloader = Downloader(media)
    return downloader.start_download()
