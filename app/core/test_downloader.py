import unittest
from pathlib import Path

from .downloader import Downloader
from .env import get_env
from .media import Media


class TestDownloaderCase(unittest.TestCase):
    url_video = get_env('URL_VIDEO')
    media: Media
    downloader: Downloader
    
    def setUp(self):
        self.media = Media(self.url_video)
        self.downloader = Downloader(self.media)

    def test_start_download(self):
        output_path = self.downloader.start_download()
        self.assertTrue(output_path.exists())
        
    def test_start_download_with_output_dir(self):
        output_dir = Path('/tmp/downloads')
        self.downloader = Downloader(self.media, output_dir)
        
        output_path = self.downloader.start_download()
        self.assertTrue(output_path.exists())

if __name__ == '__main__':
    unittest.main()
