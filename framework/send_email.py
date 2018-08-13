# -*- coding: utf-8 -*-
__author__ = 'tyr'
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication

class SendEmail(object):
    def send_email(self, title, mail_from, mail_to, pwd, content, smtp_server, port, excel_path, excel_name, jpg_path,jpg_name):
        # 生成包含多个邮件体的对象
        msg = email.mime.multipart.MIMEMultipart()
        msg['From'] = mail_from
        msg['To'] = mail_to
        msg['Subject'] = title
        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)
        #excel附件--固定格式
        xlsxpart = MIMEApplication(open(excel_path, 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename=excel_name)
        msg.attach(xlsxpart)
        #jpg图片附件
        jpgpart = MIMEApplication(open(jpg_path, 'rb').read())
        jpgpart.add_header('Content-Disposition', 'attachment', filename=jpg_name)
        msg.attach(jpgpart)
        #发送邮件
        smtp = smtplib.SMTP(smtp_server, port)
        #设置为调试模式，console中显示
        smtp.set_debuglevel(1)
        #连接服务器，smtp地址+端口，qq:smtp.qq.com+465或者587,126：smtp.126.com+25
        ''' oxmail邮箱服务器的端口号如下：
            1、POP3/SMTP协议
            接收邮件服务器：pop.exmail.qq.com (端口 110)，使用SSL，端口号995
            发送邮件服务器：smtp.exmail.qq.com (端口 25)，使用SSL，端口号465或587
            2、IMAP协议
            接收邮件服务器：imap.exmail.qq.com (端口 143)，使用SSL，端口号993
            发送邮件服务器：smtp.exmail.qq.com (端口 25)，使用SSL，端口号465或587'''
        # smtp.connect('smtp.126.com', '25')   写到smtp = smtplib.SMTP('smtp.126.com', '25')了
        smtp.starttls()#可能发送失败，加这句试试
        smtp.login(mail_from, pwd)
        #发送，from+to+内容
        smtp.sendmail(mail_from, mail_to, str(msg))
        smtp.quit()
        print('发送邮件成功')


