import os
import src.logger
from src.client import Client
from src.text import load_text
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    load_text()
    client = Client()