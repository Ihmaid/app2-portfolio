import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "teste1111python@gmail.com"
password = "bwck hrci xerb ypik"
receiver = "datadynamogmb@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
