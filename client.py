import os
from dotenv import load_dotenv

load_dotenv()

IMAGE_DIR = "./images"
SERVER_URL = os.getenv("SERVER_URL")
CAPTURE_DELAY = int(os.getenv("CAPTURE_DERAY", 1))
