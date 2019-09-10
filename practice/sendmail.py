#!/usr/bin/python
import smtplib

sender = 'praneeth@digitalinterakt.com'
receivers = ['praneeth@digitalinterakt.com']

message = """From: From Praneeth <praneeth@digitalinterakt.com>
To: To Praneeth <praneeth@digitalinterakt.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('digitalinterkt.com',25)
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except Exception:
   print("Error: unable to send email")