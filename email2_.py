#!/usr/bin/env python3
# Protocol for getting email: IMAP 
# Search for your email provider's IMAP server domain name
# Less Secure app settings for Gmail: https://myaccount.google.com/lesssecureapps
# pip install IMAPClient
# pip install pyzmail
import imapclient
import pyzmail
from email_credentials import *
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True) 
conn.login(MAIL_FROM, MAIL_FROM_PASS) # email address, password
conn.list_folders() # the third value of every tuple will indicate the folder name
conn.select_folder('INBOX', readonly=True) # readonly = True can't delete any mail

# to know more about the criterias link: https://imapclient.readthedocs.io/en/master/#imapclient.IMAPClient.search
UIDs = conn.search(['SINCE' , '20-Aug-2015']) # list of UIDs of the emails, select any of the UID & use like below 
# UIDs = conn.search(['FROM' , 'farhan.tanvir.utshaw@gmail.com'])

# conn.delete_messages([47474, 47475]) # list of UIDs of the mails that needs to be deleted, will only work if readonly=False


if len(UIDs) > 0:
    rawMessage = conn.fetch([UIDs[-1]], ['BODY[]', 'FLAGS']) # I am using the very last UID
    message = pyzmail.PyzMessage.factory(rawMessage[UIDs[-1]][b'BODY[]'])
    mail_subject = message.get_subject() # subject of the message
    mail_from = message.get_address('from') # tuples contaning username, email address of the sender
    mail_to = message.get_address('to') # to whom the mail was sent
    mail_bcc = message.get_address('bcc')
    isHTMLMail = message.html_part # returns None if no HTML is used in the mail
    isTextMail = message.text_part  # returns None if no text portion is used in the mail
    mailTextPart = message.text_part.get_payload().decode('UTF-8')
    print('Mail Subject: ' + mail_subject)
    print('Mail From: ' + str(mail_from))
    print('Mail To: ' + str(mail_to))
    print('Mail bcc: ' + str(mail_bcc))
    print('Mail Text Part')
    print('-'*25)
    print(mailTextPart)

    conn.logout()

    print()
else:
    print('No email found for your criteria')
