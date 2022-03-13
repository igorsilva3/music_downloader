import unittest
from pathlib import Path

from .downloader import Downloader
from .media import Media


class TestDownloaderCase(unittest.TestCase):
    url_video = 'https://www.youtube.com/watch?v=SivKcsEDNNY'
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
