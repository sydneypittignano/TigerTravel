#!/usr/bin/env python

#-----------------------------------------------------------------------
# emails.py
# Author: Owen Travis
# Sources:
# https://k-h-kramp.medium.com/automate-e-mail-sending-from-heroku-with-python-a7543ea8a0b6
# https://fedingo.com/how-to-send-html-mail-with-attachment-using-python/
#-----------------------------------------------------------------------

import os
from emailtemplates import REQUEST_ACCEPTED_TEMPLATE, REQUEST_RECEIVED_TEMPLATE, REQUEST_DECLINED_TEMPLATE, RIDE_LEFT_TEMPLATE, REQUEST_CANCELLED_TEMPLATE
from keys import SENDGRID_API_KEY
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#-----------------------------------------------------------------------

# SENDGRID_API_KEY = os.environ['SENDGRID_API_KEY']

#-----------------------------------------------------------------------


# This gets called by every function below
# Do not change this
def send_message_mailgun(html, subject, recipient, sender):
    message = Mail(
        from_email=sender,
        to_emails=recipient,
        subject=subject,
        html_content=html)
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

#-----------------------------------------------------------------------

def email_request_received(recipient_netids):
    html = REQUEST_RECEIVED_TEMPLATE
    subject = "Someone has requested to join your ride!"
    sender = "princetontigertravel@gmail.com"
    for recipient_netid in recipient_netids:
        recipient = recipient_netid + "@princeton.edu"
        send_message_mailgun(html, subject, recipient, sender)
#-----------------------------------------------------------------------

def email_request_accepted(recipient_netids):
    html = REQUEST_ACCEPTED_TEMPLATE
    subject = "Your join request has been accepted!"
    sender = "princetontigertravel@gmail.com"
    for recipient_netid in recipient_netids:
        recipient = recipient_netid + "@princeton.edu"
        send_message_mailgun(html, subject, recipient, sender)

#-----------------------------------------------------------------------

def email_request_declined(recipient_netids):
    html = REQUEST_DECLINED_TEMPLATE
    subject = "Your join request has been declined."
    sender = "princetontigertravel@gmail.com"
    for recipient_netid in recipient_netids:
        recipient = recipient_netid + "@princeton.edu"
        send_message_mailgun(html, subject, recipient, sender)

#-----------------------------------------------------------------------

def email_ride_left(recipient_netids):
    html = RIDE_LEFT_TEMPLATE
    subject = "Someone has left your ride."
    sender = "princetontigertravel@gmail.com"
    for recipient_netid in recipient_netids:
        recipient = recipient_netid + "@princeton.edu"
        send_message_mailgun(html, subject, recipient, sender)

def email_request_cancelled(recipient_netids):
    html = REQUEST_CANCELLED_TEMPLATE
    subject = "Someone has cancelled a request to join your ride."
    sender = "princetontigertravel@gmail.com"
    for recipient_netid in recipient_netids:
        recipient = recipient_netid + "@princeton.edu"
        send_message_mailgun(html, subject, recipient, sender)




