import smtplib


def Send_Email(subject, msg):
    
    try:

        email_user = 'ashutoshgunjal1994@gmail.com'
        email_send = 'ashutoshgunjal1994@gmail.com'
        
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(email_user, '$$ashu1234')
        message = 'Subject: {} \n\n {}'.format(subject, msg)
        server.sendmail(email_user, email_send, message)
        server.quite()
        print("Success: Email Sent!")
    
    except:
       print ("Email failed to send")

subject = "Test Python Script"
msg = "Python script successfully emailed"
