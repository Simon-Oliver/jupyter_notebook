from pathlib import Path
import base64
import os

# print(Path.cwd())
# for file in os.walk("./images"):
#     for image in file[2]:
#         with open(f"./images/{image}", "rb") as f:
#             with open(f'./images/{image}.txt', "wb") as t:
#                 t.write(base64.b64encode(f.read()))

with open("./images/austin-wade-X6Uj51n5CE8-unsplash.jpg.txt", "r") as f:
    with open("test.jpg", "wb") as img:
        bytesImg = f.read().encode('utf-8')
        img.write(base64.decodebytes(bytesImg))
