# -*- encoding : utf-8 -*-
# @Author : 日落了
# @ Motto : 天不生python,IT 万古如长夜
# @project_name : DUOyi
# @Time : 2022/1/9
# @description : 发送qq邮件


# coding:utf -8

import smtplib  # smtp服务器
from email.mime.text import MIMEText  # 邮件文本
import time


# 邮件构建
def func():
    subject = "linux报告"  # 邮件标题
    sender = "jonathon_sunset@163.com"  # 发送方
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    content = f"该睡觉了，现在是北京时间：{time_stamp}"
    recver = "jonathon_sunset@163.com"  # 接收方
    password = "DJJYHUDMZQZBPJVM"
    # 邮箱密码
    message = MIMEText(content, "plain", "utf-8")
    # content 发送内容     "plain"文本格式   utf-8 编码格式

    message['Subject'] = subject  # 邮件标题
    message['To'] = recver  # 收件人
    message['From'] = sender  # 发件人

    smtp = smtplib.SMTP_SSL("smtp.163.com", 994)  # 实例化smtp服务器
    smtp.login(sender, password)  # 发件人登录
    smtp.sendmail(sender, [recver], message.as_string())  # as_string 对 message 的消息进行了封装
    smtp.close()


if __name__ == '__main__':
    func()
