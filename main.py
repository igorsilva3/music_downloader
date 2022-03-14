import sys

from app.main import App

app = App()

def menu():
    print("""
		1. Download of music by url video
		2. Quit
	""")

    option = str(input("Enter your option: "))

    if option == "1":
        url = str(input("Enter the url video: "))
        app.download_music(url)
        print("\nDownload complete!")
    elif option == "2":
        sys.exit()


def main():

    menu()


if __name__ == '__main__':
    main()
    sys.exit()
