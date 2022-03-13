from pathlib import Path

from .media import Media


class Downloader():
    __media: Media
    __output_dir: Path 
    __type_file = 'mp3'
    
    def __init__(self, media: Media, output_dir: Path = ''):
        self.__media = media
        self.__output_dir = output_dir or Path.cwd().joinpath('downloads')

    def start_download(self) -> Path:
        """ Return the path of the downloaded file """
        filename = f'{self.__media.title}.{self.__type_file}'
        output_path: Path = self.__output_dir.joinpath(filename)
        
        self.__media.streams.get_audio_only().download(self.__output_dir, filename=filename)
        
        return output_path
