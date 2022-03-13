import os

from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()

def get_env(key: str) -> str or None:
    """ Return the value of the environment variable """
    return os.environ.get(key)
