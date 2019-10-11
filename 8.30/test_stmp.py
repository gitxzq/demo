#-*-coding:utf-8-*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr,formataddr
from email import encoders


def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

# from_addr=input('From:')
# password=input('Password:')
# to_addr=input('to:')
# smtp_server=input('smtp server:')

from_addr='x7652514@163.com'
password='Xue7652514'
to_addr='416534352@qq.com'
smtp_server='smtp.163.com'


message=MIMEMultipart()
boby='''
<html><body><h1>Hello</h1>
<p>send by <a href="http://www.python.org">Python</a>...</p> 
</body></html>
'''
mail_body=MIMEText(boby,'html','utf8')
message['subject']=Header('来自大自然的问候','utf-8').encode()

message['from']=_format_addr('python 爱好者<%s>'%from_addr)
message['to']=_format_addr('test<%s>'%to_addr)


# message.attach(MIMEText('send with file ...','html','utf-8'))



# with open("C:/Users/Public/Pictures/Sample Pictures/Chrysanthemum.jpg","rb") as f:
#     mime=MIMEBase('image','jpg',filename='Chrysanthemum.jpg')
#     mime.add_header('Content-Disposition','attachment',filename='Chrysanthemum.jpg')
#     mime.add_header('Content-ID','<0>')
#     mime.add_header('X-Attachement-Id','0')
#
#     mime.set_payload(f.read())
#
#     encoders.encode_base64(mime)
#
#     message.attach(mime)



try:
    smtpObj=smtplib.SMTP(smtp_server,25)
    smtpObj.set_debuglevel(1)
    smtpObj.login(from_addr,password)
    smtpObj.sendmail(from_addr,[to_addr],message.as_string())
    print('邮件发送成功')
    smtpObj.quit()
except smtplib.SMTPException:
    print('邮件无法发送')