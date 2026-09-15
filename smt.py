import smtplib

smtObj= smtplib.SMTP("smtp.gmail.com",587)
smtObj.ehlo()
smtObj.starttls()
smtObj.login("aditya65489@gmail.com", "Password")
smtObj.sendmail("aditya65489@gmail.com", "aaditya65489@gmail.com", "subject: SMTP check \nThis is a sample message")
smtObj.quit()
