import unittest

from .media import Media


class TestMediaCase(unittest.TestCase):
    url_video = 'https://www.youtube.com/watch?v=SivKcsEDNNY'
    media: Media
    
    def setUp(self):
        self.media = Media(self.url_video)

    def test_get_media_info(self):
        map(lambda value: self.assertIsNotNone(value), self.media.__dict__.values())
        
        self.assertIsInstance(self.media, Media)
        
if __name__ == '__main__':
    unittest.main()
