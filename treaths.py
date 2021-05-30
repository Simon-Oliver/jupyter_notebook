import requests
import json
import concurrent.futures

baseUrl = "https://jsonplaceholder.typicode.com/photos/"
urls = []

for i in range(0, 21):
    urls.append((i, f"{baseUrl}{i+1}"))


def get_photo_url(data: tuple):
    r = requests.get(data[1])
    image_url = r.json()["url"]
    image = requests.get(image_url)
    with open(f"test_img/sample_image{data[0]}.png", "wb") as f:
        f.write(image.content)
        print(f"Image {data[0]} done")


with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    for url in urls:
        executor.submit(get_photo_url, url)
