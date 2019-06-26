#to send mail to a person using python
#--------------------------------------------------------------------
#!!!enable low security in gmail account of sender
#if using amazon or any cloud it will send a security alert first time just fix it and it will work
#--------------------------------------------------------------------
#!/usr/bin/env python3
import smtplib

gmail_user = 'Your_gmail'
gmail_app_password = 'passwd_of_your_gmail_accnt'

sent_from = gmail_user
sent_to = ['recevier_gmail']
sent_subject = "subject"
sent_body = ("message")

email_text ="""\ 
From: %s
To: %s
Subject:%s

%s
""" %(sent_from,sent_to,sent_subject,sent_body)
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)
