#!/usr/bin/env python3
# Protocol for sending mail: SMTP (Simple Mail Transfer Protocol)
import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587) # domain, port number
conn.ehlo() # start the connection, 
conn.starttls()  # TLS encryption
conn.login('')
