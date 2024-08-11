import os
import time
import imageio
import pyglet
from dotenv import load_dotenv
from dotenv import load_dotenv
import requests

load_dotenv()

IMAGE_DIR = "./images"
SERVER_URL = os.getenv("SERVER_URL")
CAPTURE_DELAY = int(os.getenv("CAPTURE_DELAY", 1)) #テスト用に環境変数から読み込めるようにしている

os.makedirs(IMAGE_DIR, exist_ok=True)
camera = imageio.imread('<video0>')
window = pyglet.window.Window(width=640, height=480)

def sendToServer(filename):
    with open(filename, "rb") as file:
        files = {'file': file}
        try:
            response = requests.post(SERVER_URL, files=files)
            response.raise_for_status()
            print("image sent to server successfully:", filename)
        except requests.exceptions.RequestExeption as e:
            print("Error sending image to server:", e)

            def captureAndSend():
                        frame = camera.get_next_data()
                        filename = os.path.join(IMAGE_DIR, f"image-{int(time.time())}.jpg")
                        imageio.imwrite(filename, frame)
                        sendToServer(filename)
                        pyglet.clock.schedule_interval(captureAndSend, CAPTURE_DELAY)
                        pyglet.app.run()

                        camera.close()





                        






         
            
            

