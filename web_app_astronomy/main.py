import streamlit as st
import requests

api_key = "uFb8po6IMWidhHmBCbw4Wi8rMa1Kxf0aIwKGHUzG"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
content = request.json()

title = (content['title'])
body = (content['explanation'])
image_url = (content['url'])

response = requests.get(image_url)
with open("image.jpg", "wb") as file:
    file.write(response.content)

# st.set_page_config(layout="centered")
st.title(title + "\n")
st.image("image.jpg")
st.write(body)

