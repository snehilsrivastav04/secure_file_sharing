import smtplib
from email.message import EmailMessage
import os

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

def send_verification_email(to_email: str, token: str):
    msg = EmailMessage()
    msg["Subject"] = "Verify your email"
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg.set_content(f"Click here to verify: http://example.com/verify?token={token}")

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
