import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "sharatkhanna@gmail.com"
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()
    receiver_email = "sharatkhanna@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)


password = os.getenv("PASSWORD")
print(password)
