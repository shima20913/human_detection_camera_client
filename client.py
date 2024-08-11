import os
import cv2
from dotenv import load_dotenv

load_dotenv()

IMAGE_DIR = "./images"
SERVER_URL = os.getenv("SERVER_URL")
CAPTURE_DELAY = int(os.getenv("CAPTURE_DERAY", 1))

os.mkdirs(IMAGE_DIR, exist_ok=True)
capt = cv2.VideoCapture(0)
if not cap.isOpened():
    print("failed open camera")
    exit()
