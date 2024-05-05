import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "sharatkhanna@gmail.com"
    password = "ovpd sdbr vqnu jwrq"
    context = ssl.create_default_context()
    receiver_email = "sharatkhanna@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)

