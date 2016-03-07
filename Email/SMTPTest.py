#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = '18627947930@163.com'
password = 'zxh3221952'

to_addr = '462451377@qq.com'

smtp_server = 'smtp.163.com'

# msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
# # 我们编写了一个函数_format_addr()来格式化一个邮件地址。
# # 注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
# msg['From'] = _format_addr('Python爱好者 <%s>' % '406426908@qq.com')
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
#
#
#
# import smtplib
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# with open('sina.html', 'rb') as f:
#     s = f.read()
#
# s = s.decode('gbk')
#
# msg = MIMEText(s, 'html', 'utf-8')
# # 我们编写了一个函数_format_addr()来格式化一个邮件地址。
# # 注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
# msg['From'] = _format_addr('Python爱好者 <%s>' % '406426908@qq.com')
# msg['To'] = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()



# import smtplib
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# l = ['abc']
# t = tuple(l)
# print(t)

# 发送附件
# 邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自xxx', 'utf-8').encode()

# 邮件正文是MIMEText
# msg.attach(MIMEText('send by zxh', 'plain', 'utf-8'))


# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('100.jpeg', 'rb') as f:
    mime = MIMEBase('image', 'jpeg', filename='100.jpeg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='100.jpeg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 读入附件内容
    mime.set_payload(f.read())
    # 用Base64编码
    encoders.encode_base64(mime)
    # 加到MIMEMultipart
    msg.attach(mime)

msg.attach(MIMEText('<html><body><h1>Hello</h1>' + '<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8'))


# 同时支持HTML和Plain格式
# 在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件
# msg = MIMEMultipart('alternative')
# msg['From'] = ...
# msg['To'] = ...
# msg['Subject'] = ...
#
# msg.attach(MIMEText('hello', 'plain', 'utf-8'))
# msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



