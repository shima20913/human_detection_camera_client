from io import BytesIO
import os
import time
import pygame
import pygame.camera
from dotenv import load_dotenv
import requests

load_dotenv()

IMAGE_DIR = "./images"
SERVER_URL = os.getenv("SERVER_URL")
CAPTURE_DELAY = int(os.getenv("CAPTURE_DELAY", 1)) #テスト用に環境変数から読み込めるようにしている

os.makedirs(IMAGE_DIR, exist_ok=True)
pygame.init()
pygame.camera.init()

if not pygame.camera.list_cameras():
    print("No camera detected.")
    pygame.quit()
    exit()
    
camera = pygame.camera.Camera(pygame.camera.list_cameras()[0], (640, 480))
camera.start()

def sendToServer(image_data):
    try:
        files = {'file': ('image.jpg', image_data, 'image/jpeg')}
        response = requests.post(SERVER_URL, files=files)
        response.raise_for_status()
        print("image sent to server successfully:")
    except requests.exceptions.RequestException as e:
        print("Error sending image to server:", e)

    def captureAndSend():
                while True:
                        image = camera.get_image()
                        image_data = BytesIO()
                        pygame.image.save(image, image_data)
                        image_data.seek(0)
                        sendToServer(image_data)
                        time.sleep(CAPTURE_DELAY)
                        
    if __name__ == "__main__":
                try:
                 captureAndSend()
                finally:
                 camera.stop()
                 pygame.quit()






                        






         
            
            

