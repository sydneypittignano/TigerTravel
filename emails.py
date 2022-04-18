#!/usr/bin/env python

#-----------------------------------------------------------------------
# emails.py
# Author: Owen Travis
# Sources:
# https://k-h-kramp.medium.com/automate-e-mail-sending-from-heroku-with-python-a7543ea8a0b6
# https://fedingo.com/how-to-send-html-mail-with-attachment-using-python/
#-----------------------------------------------------------------------

import smtplib
from email.mime.text import MIMEText
from keys import MAILGUN_SMTP_LOGIN, MAILGUN_SMTP_PASSWORD, MAILGUN_SMTP_PORT, MAILGUN_SMTP_SERVER
from emailtemplates import REQUEST_RECEIVED_TEMPLATE

#-----------------------------------------------------------------------

# This gets called by every function below
def send_message_mailgun(html, subject, recipient, sender, smtp_login, password, smtp_server, port):
    msg = MIMEText(html, "html")
    msg['Subject'] = subject
    msg['To'] = recipient
    msg['From'] = sender
    s = smtplib.SMTP(smtp_server, port)
    s.login(smtp_login, password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

#-----------------------------------------------------------------------

def email_request_received(recipient_netids):
    html = REQUEST_RECEIVED_TEMPLATE
    subject = "Someone has requested to join your ride!"
    sender = "TigerTravel <admin@princetontigertravel.herokuapp.com>"
    smtp_login = MAILGUN_SMTP_LOGIN
    smtp_server = MAILGUN_SMTP_SERVER
    password = MAILGUN_SMTP_PASSWORD
    port = MAILGUN_SMTP_PORT
    for recipient_netid in recipient_netids:
        recipient = str(recipient_netid) + "@princeton.edu"
        print(recipient)
        send_message_mailgun(html, subject, recipient, sender, smtp_login, password, smtp_server, port)