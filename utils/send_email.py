import os, logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(name, email, message):
    sender_email = "admin@keenai.io"
    receiver_email = "vince@keenai.io"
    app_password = os.getenv("APP_PASSWORD")
    logging.info('APP PASSWORD: %s', app_password)  # Correctly formatted log message

    if app_password is None:
        logging.error("APP_PASSWORD environment variable is not set")
        return False

    logging.info("APP_PASSWORD is set to: %s", app_password)  # Correctly formatted log message

    # Create the email content
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = f"New Contact Us Message from {name}"

    # Create the email body
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        logging.error("Error sending email: %s", str(e))
        return False

