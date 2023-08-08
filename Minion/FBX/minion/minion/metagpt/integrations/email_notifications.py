import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailAPI:
    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def send_email_notification(self, email, subject, message):
        # Send email notification using email API
        msg = MIMEMultipart()
        msg['From'] = 'your_email'
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP('your_smtp_server', your_smtp_port) as server:
            server.starttls()
            server.login('your_email', 'your_password')
            server.send_message(msg)