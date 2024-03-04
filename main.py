import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email(subject, body):
    sender_email = "sender@example.com"
    receiver_email = "receiver@example.com"
    password ="password"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
def detection():
     try:
        socket.create_connection(("127.0.0.1", 80), timeout=30)
     except Exception:
        send_email("Intrusion Alert!", "Failed attempt to connect to the specified IP address.")

if __name__ == "__main__":
    detection()
