# -*- coding: utf-8 -*-
# @Author ：Mingjie Huang
# @Time   ：2019/7/4 18:43
# @IDE    ：PyCharm

import os
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from comm.readdoc import read_config


def insert_img(driver, filename):
    '''
    生成屏幕截图
    :param driver:
    :param filename:
    :return:
    '''
    func_path = os.path.dirname(__file__)
    # print(func_path)
    base_dir = os.path.dirname(func_path)
    # print(base_dir)

    # 将路径转化为字符串
    base_dir = str(base_dir)

    # 对路径的字符串进行替换
    base_dir = base_dir.replace('\\', '/')
    # print(base_dir)

    base = base_dir.split('/Website')[0]

    # print(base)
    filepath = base + '/Website/test_report_dongguan/screenshot/' + filename
    # print(filepath)
    driver.get_screenshot_as_file(filepath)


def send_mail(latest_report):
    '''
    发送测试报告邮件
    :param latest_report:
    :return:
    '''
    # 将对应SMTP的配置信息进行赋值
    # email_config = ReadConfig()
    # print(email_config)
    smtp_server = read_config('comm', 'email_server')
    smtp_port = read_config('comm', 'email_server_port')
    user = read_config('comm', 'email_username')
    password = read_config('comm', 'email_passwd')
    email_receives = read_config('comm', 'email_receiver')

    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()

    receives = email_receives.split(',')
    # print(receives)

    subject = '自动化测试报告'

    # 构造附件内容

    att = MIMEText(mail_content, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="result.html"'

    # 构建发送与接收信息
    msg = MIMEMultipart()
    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
    msg['subject'] = subject
    msg['From'] = user
    msg['To'] = ','.join(receives)
    msg.attach(att)

    # msg = MIMEText(mail_content, _subtype='html', _charset='utf-8')
    # msg['Subject'] = Header(subject, 'utf-8')
    # msg['From'] = user
    # msg['To'] = ','.join(receives)

    # 建立连接
    smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    smtp.helo(smtp_server)
    smtp.ehlo(smtp_server)
    smtp.login(user, password)

    print("Start send email...")
    # 发送邮件
    smtp.sendmail(user, receives, msg.as_string())
    smtp.quit()
    print("Send email end!")


def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-1])
    # 输出最新报告的路径
    file = os.path.join(report_dir, lists[-1])
    return file