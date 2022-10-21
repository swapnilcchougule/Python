#!/usr/bin/python3

# Simple Mail Transfer Protocol (SMTP)
# https://docs.python.org/3/library/smtplib.html#smtp-example
# https://www.tutorialspoint.com/python3/python_sending_email.htm
# https://www.youtube.com/watch?v=JRCJ6RtE3xU&t=306s&ab_channel=CoreySchafer
# https://www.youtube.com/watch?v=NvtjLXSY-hE&ab_channel=LianneandJustin
# https://www.youtube.com/watch?v=sHJt3ROfij4&ab_channel=PythonTrends
# turn "ON" Less secure app access 


# Import modules
import smtplib, ssl, csv
from email.message import EmailMessage

# Please replace below with your email address and password
email_from = 'sender_email@gmail.com'
password = 'xxx'
email_to = 'receiver_email@gmail.com'
subject = 'This is subject form SMTP code'
msg = ''' Hello \n
This is message form SMTP code \n

Regards,
Swapnil '''

# establish connection to service privider, establish server connection
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()                               
server.login(email_from, password)

email = EmailMessage()      # create a object of EmailMessage
email['From'] = email_from
email['To'] = email_to
email['Subject'] = subject
email.set_content(msg)

server.send_message(email)
print("Email sent successfully...!")
server.close()

