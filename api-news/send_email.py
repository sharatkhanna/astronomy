import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "sharatkhanna@gmail.com"

    context = ssl.create_default_context()
    receiver_email = "sharatkhanna@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, os.getenv("PASSWORD"))
        server.sendmail(username, receiver_email, message)


if __name__ == "__main__":
    send_email("Hi This is a test message")

