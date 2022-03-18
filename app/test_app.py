import unittest
from pathlib import Path

from .core.env import get_env
from .main import App


class TestAppCase(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.video_url = get_env('URL_VIDEO')
        self.file_path = Path(get_env('FILE_PATH'))
        
    def test_download_music(self):
        file_path = self.app.download_music(self.video_url)
        
        self.assertTrue(file_path.exists())
        
    def test_download_musics_by_file(self):
        
        folder_name = 'Guitar Hero III'
        
        output_dir = self.app.download_musics_by_file(folder_name, self.file_path)
        
        self.assertTrue(output_dir.exists())
        
    def test_download_musics_by_file_not_found(self):
        folder_name = 'Guitar Hero III'
        file_path = get_env('FILE_PATH_NOT_FOUND')
        
        self.assertRaises(FileNotFoundError, self.app.download_musics_by_file, folder_name, file_path)

    def test_download_all(self):
        output_dirs = self.app.download_all(self.file_path)
        
        self.assertIsInstance(output_dirs, list)
        self.assertTrue(len(output_dirs) > 0)
        self.assertIsInstance(output_dirs[0], Path)
        map(lambda output_dir: self.assertTrue(output_dir.exists()), output_dirs)
