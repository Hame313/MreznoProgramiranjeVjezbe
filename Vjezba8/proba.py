
import smtplib 
  
 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
sender_email_id="beganhame@gmail.com"
sender_email_id_password= "12345"
receiver_email_id="marioperdul@hotmail.com"
s.starttls() 
  
# Authentication 
s.login("sender_email_id", "sender_email_id_password") 
  
# message to be sent 
message = "Halo jel stiglo sta?"
  
# sending the mail 
s.sendmail("sender_email_id", "receiver_email_id", message) 
  
# terminating the session 
s.quit() 
