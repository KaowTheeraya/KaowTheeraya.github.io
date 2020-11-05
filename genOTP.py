import sys
import math
from otpauth import OtpAuth
import smtplib
import requests

count=5

val="kaow"

def otp():
    auth = OtpAuth(val)
    res = auth.totp()
    return res

def send_email(mailto,subject,msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        sender_email = 'Jimjum.Gameshop@gmail.com'
        sender_password = 'jimjimjum'
        server.login(sender_email,sender_password)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(sender_email,mailto,message)
        server.quit()
        print('Success : Email sent !')
    except:
        print('Fail : Email not sent')

a = otp()
topic =  ' Your OTP for Jimjum GameShop ! '
bonus = sys.argv[1]
test = """  Hi, I'm an adminstrator from Jimjum GameShop! nice to meet you.  
        your OTP is : """ + str(a) + """ : Hope you enjoy it ! Have fun ^_^ """
print(test)
send_email(bonus,topic,test)
print (sys.argv[1])
print (a)
