import requests
responce = requests.get("https://www.youtube.com/watch?v=Nsb3bLIlO4w&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=89")
print(responce.text)