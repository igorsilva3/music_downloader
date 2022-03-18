import json
from pathlib import Path


class ReaderFileJSON:
    def __init__(self, file_path: Path):
        self.__file = open(file_path, 'r')
        self.__file_content = self.__read_file()

    def __del__(self):
        self.__file.close()

    def __read_file(self) -> dict:
        """ Return the file content. """
        return json.load(self.__file)

    def get_content(self) -> dict:
        """ Return the content of the file. """
        return self.__file_content

    def get_folder_names(self) -> str:
        """ Return the folder names from the file. """
        folder_names = [
            folder_name for folder_name in self.__file_content.keys()]

        return folder_names

    def get_music(self, folder_name: str,) -> dict:
        """ Return the music from the file. """
        music = {
            'folder_name': folder_name,
            'urls': self.__file_content.get(folder_name)
        }

        return music
