from src.alias import load_aliases
from src.text import load_text
from dotenv import load_dotenv

VERSION = "0.0.1"

if __name__ == "__main__":
    load_dotenv()
    load_aliases()
    load_text()
    
    from src.client import Client
    client = Client()
    client.run()