import sys
from pathlib import Path
from time import sleep

import colorful as cf
import emoji

from app.main import App

app = App()

CENTRALIZED = 65
FILE_PATH = Path().cwd().joinpath('musics.json')


def menu():
    options = {
        '1': 'Download music by url',
        '2': 'Download of music by file (All)',
        '3': 'Download of music by file (Partial)',
        '4': 'Quit'
    }

    print('')
    for option, action in options.items():
        print(cf.italic & cf.green |
              f"{option}. {action}\n".center(CENTRALIZED))

    option = str(input(cf.yellow | "\nEnter your option: "))

    return option


def action_download_music_by_url():
    url = str(input(cf.yellow | "\nEnter the url video: "))
    file_path = app.download_music(url)

    print(cf.green | f"\nDownload complete!\n\n{cf.italic & cf.orange}Music path: {file_path}\n".center(
        CENTRALIZED))


def action_download_music_by_file_all():
    print(cf.orange | f"\nFile found: {cf.italic | FILE_PATH}")

    output_dirs = app.download_all(FILE_PATH)

    for output_dir in output_dirs:
        print(cf.green | f"\nDownload complete!\n\n{cf.italic & cf.orange}Music path: {output_dir}".center(
            CENTRALIZED))
        sleep(1.5)

    print('')


def action_download_music_by_file_partial():
    print(cf.orange | f"\nFile found: {cf.italic | FILE_PATH}")

    folder_name = str(input(cf.yellow | "\nEnter the key in the file: "))

    output_dir = app.download_musics_by_file(folder_name, FILE_PATH)

    print(cf.green | f"\nDownload complete!{cf.italic & cf.orange}\n\nOutput dir: {output_dir}\n".center(
        CENTRALIZED))


def action_quit():
    print(cf.green | emoji.emojize(
        "\nGood Bye!!! :beaming_face_with_smiling_eyes: \n".center(CENTRALIZED)))
    sleep(1)
    sys.exit()


def main():
    option = menu()

    options = {
        '1': action_download_music_by_url,
        '2': action_download_music_by_file_all,
        '3': action_download_music_by_file_partial,
        '4': action_quit,
    }

    options.get(option, lambda: (
        print(cf.bold & cf.red | "Invalid option!\n".center(65))))()


if __name__ == '__main__':
    main()
    sys.exit()
