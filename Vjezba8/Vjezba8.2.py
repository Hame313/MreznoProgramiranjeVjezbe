import smtplib
 

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
port = 587
smtp_server = "smtp.gmail.com"
login = "beganhame@gmail.com" 
password = "12345" 
 
subject = "Primjer"
sender_email = "beganhame@gmail"
receiver_email = "marioperdul@gmail.com"
 
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
 

body = "Jel stiglo"
message.attach(MIMEText(body, "plain"))
 
filename = "tcp_client.py"

 

with open(filename, "rb") as attachment:
    
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
 

encoders.encode_base64(part)
 
 
part.add_header(
    "Content-Disposition",
    "attachment; filename= {filename}",
)
 

message.attach(part)
text = message.as_string()
 

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.login(login, password)
    server.sendmail(
        sender_email, receiver_email, text
    )
print('Sent') 