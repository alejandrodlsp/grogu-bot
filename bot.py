import os
from dotenv import load_dotenv

from src.client import Client

if __name__ == "__main__":
    load_dotenv()
    client = Client()