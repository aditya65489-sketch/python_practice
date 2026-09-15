import smtplib

smtObj= smtplib.SMTP_SSL("smtp.gmail.com",587)
smtObj.ehlo()
smtObj.starttls()
smtObj.login("aditya5489@gmail.com", "password")
smtObj.sendmail("aditya65489@gmail.com", "aaditya65489@gmail.com", "subject: \nThis is a sample message")
smtObj.quit()
