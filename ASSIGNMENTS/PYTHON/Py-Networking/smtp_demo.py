
import smtplib

sender = 'vigneshram0706@gmail.com'
receivers = ['223003109@sastra.ac.in']

message = """From: From Person <vigneshram0706@gmail.com>
To: To Person <223003109@sastra.ac.in>
Subject: SMTP e-mail test 2

This is a test e-mail message.
"""
print("hello")
try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except smtplib.SMTPException:
   print("Error: unable to send email")