import requests
from pathlib import Path

# image_path = Path(__file__).parent / "./test/fruit.jpg"
image_path = Path(__file__).parent / "./test/device.jpg"

url = "http://127.0.0.1:8000"
files = {"image": open(image_path, "rb")}
response = requests.post(url, files=files)
print(response.text)