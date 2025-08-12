import requests
import json

query = input("what type of news are you intrested in ?  ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-17&sortBy=publishedAt&apiKey=9917f06f0c274017aa7d2a7d94224923"
r = requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------------------------------------")


