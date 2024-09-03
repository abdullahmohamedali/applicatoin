import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from api import Description, Title, Image
from main import message


# Email setup
sender_email = "abdullah.khafagy2@gmail.com"
receiver_email = "abdullah.khafagy2@gmail.com"
password = "zakw lujj xjus waex"

# Create the email content
subject = "Latest News Articles"
# body = f"""
# Here are the latest news articles:
#
# 1. Title: Article {Title}
#    Description: {Description}
#
# """

html = f"""
<html>
  <body>
    <p>Here are the latest news articles:</p>
    <ul>
      <li>{message}</li>
    </ul>
    <p>Here is an image for you:</p>
    <img src="{Image}" alt="Image" width="500">
  </body>
</html>
"""

# Create a MIME object
message = MIMEMultipart("alternative")
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the body text
# message.attach(MIMEText(body, 'plain'))
part = MIMEText(html, "html")
message.attach(part)
# Sending the email
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
