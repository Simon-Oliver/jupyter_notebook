import requests
import json

webhook_url = "https://webhook.site/cdeb7ea5-22c8-4459-8b43-7b9389241638"
data = {"name": "Webhook Test", "data": "Fun Data"}

r = requests.post(webhook_url, data=json.dumps(data), headers={
                  "Content-Type": "application/json"})
