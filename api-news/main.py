import requests
from send_email import send_email

api_key = "02a5b172855946058cd430507b4b389e"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-04-08"
       "&sortBy=publishedAt&apiKey=02a5b172855946058cd430507b4b389e")

request = requests.get(url)
content = request.json()

body = ""
for article in content['articles'][0:20]:
    if article['title'] is not None:
        body = body + article['title'] + "\n" + article['description'] + "\n\n"

body = body.encode("utf-8")
print(body)
send_email(body)