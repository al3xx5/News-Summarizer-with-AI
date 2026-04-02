import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import config
import ast

def send_email(subject, body_html):
    email_list = ast.literal_eval(config.EMAIL_ADDRESS)
    sender_email = email_list[0]
    password = config.EMAIL_APP_PASSWORD

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = ""

    part = MIMEText(body_html, "html")
    msg.attach(part)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        
        server.starttls() 
        
        server.login(sender_email, password)
        
        server.sendmail(sender_email, email_list, msg.as_string())
        server.quit()
        
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Testing block to ensure mailer is working
if __name__ == "__main__":
    today_date = datetime.now().strftime("%b %d, %Y")
    test_subject = f"Test: AI Cybersecurity News for {today_date}"
    
    test_body = (
        "<h2>This is a test email</h2>"
        "<p>If you are reading this in your inbox, your <b>mailer.py</b> module and App Password are working perfectly!</p>"
    )
    
    print("Attempting to send test email...")
    send_email(test_subject, test_body)