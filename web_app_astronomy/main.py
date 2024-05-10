import streamlit as st
import requests

api_key = "uFb8po6IMWidhHmBCbw4Wi8rMa1Kxf0aIwKGHUzG"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
content = request.json()

title = (content['title'])
body = (content['explanation'])
image_url = (content['url'])

print(title)
print(image_url)
print(body)

st.title(title + "\n")

if image_url.endswith('.jpg'):
    response = requests.get(image_url)
    with open("image.jpg", "wb") as file:
        file.write(response.content)
    st.image("image.jpg")
else:
    st.write(image_url)

st.write(body)

