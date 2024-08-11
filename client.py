import os
import time
import cv2
from dotenv import load_dotenv
import requests

load_dotenv()

IMAGE_DIR = "./images"
SERVER_URL = os.getenv("SERVER_URL")
CAPTURE_DELAY = int(os.getenv("CAPTURE_DERAY", 1))

os.mkdirs(IMAGE_DIR, exist_ok=True)
capt = cv2.VideoCapture(0)
if not capt.isOpened():
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

            while True:
                        ret, frame = capt.read()
                        if not ret:
                            print("failed get capture flame")
                            break

                        filename = os.path.join(IMAGE_DIR, f"image-{int(time.time())}.jpg")
                        cv2.imwrite(filename, frame)



         
            
            

