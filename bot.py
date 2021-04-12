import os
import src.logger
from src.client import Client
from src.alias import load_aliases
from src.text import load_text
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    load_aliases()
    load_text()
    
    client = Client()
    client.run()