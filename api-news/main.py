import requests
from send_email import send_email

keyword = "tesla"
api_key = "02a5b172855946058cd430507b4b389e"
url = (f"https://newsapi.org/v2/everything?"
       f"q={keyword.lower()}"
       "&from=2024-04-10"
       "&sortBy=publishedAt"
       "&apiKey=02a5b172855946058cd430507b4b389e"
       "&language=en")

request = requests.get(url)
content = request.json()

body = ""
for article in content['articles'][3:5]:
    if article['title'] is not None:
        body = ("Subject: Top News for today\n"
                + body + article['title'] + "\n"
                + article['description'] + "\n"
                + article["url"] + "\n\n")

body = body.encode("utf-8")
print(body)
send_email(body)
