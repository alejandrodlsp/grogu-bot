import os
import src.logger
from src.client import Client
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    client = Client()