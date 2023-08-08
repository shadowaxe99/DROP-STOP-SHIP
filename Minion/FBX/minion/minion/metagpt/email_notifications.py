import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email_notification(email, subject, message):
    # Set up the SMTP server
    s = smtplib.SMTP(host='your_smtp_server', port=your_smtp_port)
    s.starttls()

    # Log in to the server
    s.login('your_email', 'your_password')

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = 'your_email'
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Send the email
    s.send_message(msg)

    # Close the connection to the server
    s.quit()