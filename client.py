import os
import cv2
from dotenv import load_dotenv
import requests

load_dotenv()

IMAGE_DIR = "./images"
SERVER_URL = os.getenv("SERVER_URL")
CAPTURE_DELAY = int(os.getenv("CAPTURE_DERAY", 1))

os.mkdirs(IMAGE_DIR, exist_ok=True)
capt = cv2.VideoCapture(0)
if not cap.isOpened():
    print("failed open camera")
    exit()

def sendToServer(filename):
    with open(filename, "rb") as file:
        files = {'file': file}
        try:
            response = requests.post(SERVER_URL, files=files)
            response.raise_for_status()
            print("image sent to server successfully:", filename)
        except requests.exceptions.RequestExeption as e:
            print("Error sending image to server:", e)