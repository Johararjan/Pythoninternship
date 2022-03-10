import smtplib
sender = input('enter sender email address')
receivers = input('enter receiver email address')
password = input('enter application specific password of sender email')
#in the above input prompt enter your google account application specific password for more details please read the
# readme.txt file
server = smtplib.SMTP('smtp.gmail.com', 587)
subject = input("enter subject")
body = input("enter body")
message = f'subject:{subject}\n\n{body}'
server.starttls()
server.login(sender, password)
print('login successfull')
server.sendmail(sender, receivers, message)
print("email sent successfully")
