import requests

api_key = "02a5b172855946058cd430507b4b389e"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-04-08"
       "&sortBy=publishedAt&apiKey=02a5b172855946058cd430507b4b389e")

request = requests.get(url)
content = request.json()

for article in content['articles']:
    print(article['title'] + ": \n")
    print(article['description'])
