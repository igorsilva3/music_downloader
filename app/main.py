from pathlib import Path

from .core.downloader import Downloader
from .core.media import Media
from .core.reader_file_json import ReaderFileJSON


class App:
    def __init__(self):
        self.output_dir = Path().cwd().joinpath('downloads')

    def download_music(self, url: str, output_dir: Path = '') -> Path:
        output_dir = output_dir or self.output_dir
        
        if output_dir.exists():
            return output_dir

        media = Media(url)
        downloader = Downloader(media, output_dir)

        return downloader.start_download()

    def download_musics_by_file(self, folder_name: str, file_path: Path) -> Path:
        if not file_path or not file_path.exists():
            raise FileNotFoundError('File not found')

        reader_file = ReaderFileJSON(file_path)
        music = reader_file.get_music(folder_name)

        output_dir = Path().cwd().joinpath('downloads', folder_name)

        downloads = [download for download in [self.download_music(
            url, output_dir) for url in music.get('urls')]]

        return output_dir
    
    def download_all(self, file_path: Path) -> list[Path]:
        reader_file = ReaderFileJSON(file_path)
        file_content = reader_file.get_content()
        output_dirs = []

        for folder_name in file_content.keys():
            output_path = self.download_musics_by_file(folder_name, file_path)
            output_dirs.append(output_path)
            
        return output_dirs
