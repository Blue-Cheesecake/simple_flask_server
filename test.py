from urllib import response
import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "helloworld")
# response = requests.post(BASE + "helloworld")

# response = requests.get(BASE + "helloname/Sprite")
# response = requests.get(BASE + "helloname/Kean")

response = requests.put(BASE + "video/1", {
    "name": "DR. Strange",
    "views": 30,
    "likes": 20,
})

response = requests.get(
    url=BASE + "/video/1"
)

print(response.json())
