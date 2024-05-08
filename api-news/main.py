import requests
from send_email import send_email

api_key = "02a5b172855946058cd430507b4b389e"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-04-08"
       "&sortBy=publishedAt&apiKey=02a5b172855946058cd430507b4b389e")

request = requests.get(url)
content = request.json()

email_content = ""
for article in content['articles'][0:3]:
    email_content = email_content + article['title'] + "\n" + article['description'] + "\n\n"

print(email_content)
# send_email(email_content)