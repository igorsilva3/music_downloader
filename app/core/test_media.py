import unittest

from .env import get_env
from .media import Media


class TestMediaCase(unittest.TestCase):
    url_video = get_env('URL_VIDEO')
    media: Media
    
    def setUp(self):
        self.media = Media(self.url_video)

    def test_get_media_info(self):
        map(lambda value: self.assertIsNotNone(value), self.media.__dict__.values())
        
        self.assertIsInstance(self.media, Media)
        
if __name__ == '__main__':
    unittest.main()
