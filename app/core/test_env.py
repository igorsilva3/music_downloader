import unittest

from .env import get_env


class TestEnvCase(unittest.TestCase):
    def test_get_env(self):
        url_video = get_env('URL_VIDEO')
        self.assertIsNotNone(url_video)

    def test_get_env_not_found(self):
        url_video = get_env('URL_VIDEO_NOT_FOUND')
        self.assertIsNone(url_video)

if __name__ == '__main__':
    unittest.main()
