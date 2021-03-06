import smtplib
from email.mime.text import MIMEText
import os


def sendMail(subject, body):

    mail_host = 'smtp.sina.com'
    mail_user = os.environ.get('MAIL_USERNAME')
    mail_pswd = os.environ.get('MAIL_PASSWORD')

    # 创建一个空邮件，下面就是放入内容
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'chengtianyang523@sina.com'
    msg['To'] = '873948000@qq.com'

    # 创建smtp实例，用smtp协议发邮件
    s = smtplib.SMTP()
    # 连接服务器，这里是新浪的
    s.connect(mail_host, 25)
    # 登陆账号，不然怎么发呢
    s.login(mail_user, mail_pswd)
    # 发邮件
    # 还有另外一种s.send_mail(sender, receiver)
    s.send_message(msg)
    # 随手关闭服务器是个好习惯哦
    s.quit()
