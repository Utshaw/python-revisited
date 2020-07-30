#!/usr/bin/env python3
# Protocol for sending mail: SMTP (Simple Mail Transfer Protocol)
# Less Secure app settings for Gmail: https://myaccount.google.com/lesssecureapps
import smtplib
from email_credentials import *

conn = smtplib.SMTP('smtp.gmail.com', 587) # SMTP service domain name, port number
print(conn.ehlo()) # start the connection, 
conn.starttls()  # TLS encryption
conn.login(MAIL_FROM, MAIL_FROM_PASS) # email address, password
conn.sendmail(MAIL_FROM, MAIL_TO, 'Subject: Utshaw\'s subject\n\n These lines constitute the body of the email\nStill inside body\n\nLines of body!!')
conn.quit()

