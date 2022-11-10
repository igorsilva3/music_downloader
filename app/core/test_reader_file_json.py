import unittest
from pathlib import Path

from .env import get_env
from .reader_file_json import ReaderFileJSON


class TestReaderFileJSONCase(unittest.TestCase):
    def setUp(self):
        self.file_path = Path().cwd().joinpath(get_env('FILE_PATH'))
        self.folder_name = get_env('FOLDER_NAME')
        
    def test_get_content(self):
        reader_file = ReaderFileJSON(self.file_path)
        file_content = reader_file.get_content()
        
        self.assertIsInstance(file_content, dict)
        self.assertIsNotNone(file_content)
        
    def test_get_folder_names(self):
        reader_file = ReaderFileJSON(self.file_path)
        folder_names = reader_file.get_folder_names()
        
        self.assertIsInstance(folder_names, list)
        self.assertIsInstance(folder_names[0], str)
        self.assertTrue(len(folder_names) > 0)
        
    def test_get_music(self):
        reader_file = ReaderFileJSON(self.file_path)
        music = reader_file.get_music(self.folder_name)
        
        self.assertIsInstance(music, dict)
        self.assertIsInstance(music['folder_name'], str)
        self.assertIsInstance(music['urls'], list)
        self.assertTrue(len(music['urls']) > 0)
        
if __name__ == '__main__':
    unittest.main()
