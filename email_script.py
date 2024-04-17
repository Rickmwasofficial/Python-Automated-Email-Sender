#import smtplib to use the smtp protocol
#import EmailMessage class
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["From"] = "Sender's email"
email["to"] = "Receiver's email"
email["subject"] = "The subject of your email"
#The contents of your Email
email.set_content("You are receiving an email from my automated python script. Kindly ignore")

#initialize the smtp protocol (simple mail transfer protocol)
#The host varies with different email services i.e gmail, outlook etc...
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
  smtp.ehlo() #handshake
  #start tls encryption
  smtp.stattls()
  #ensure you enable two factor authentication for your google account then create an access key for this script
  smtp.login("sender's_email_goes_here", "sender's_access_key_for_google_account")
  smtp.send_message(email)
  print("Email Sent!")
