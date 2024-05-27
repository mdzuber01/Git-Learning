import requests
import json
query=input("What type of news you want to display?: ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-04-24&sortBy=publishedAt&apiKey=cb94dcac7fd4415ab941831012352a35"
r=requests.get(url)
#print(r.text)
news=json.loads(r.text)
#print(news,type(news))
#print(news["articles"])
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("!!!!----------------------!!!!")