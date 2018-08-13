# -*- coding: utf-8 -*-
__author__ = 'tyr'
from framework.send_email import SendEmail
from framework.interfacetest import InterfaceTest
from framework.log import Log
# excel_path = 'E:/PythonFile/MyInterfaceTest/excels/tyr_testcase.xlsx'
# excel_name = 'tyr_testcase.xlsx'
# jpg_path = 'E:/PythonFile/MyInterfaceTest/pictures/test.jpg'
# jpg_name = 'test.jpg'
# from_email = 'xxx'
# to_email = 'xxx'
# pwd = 'xxx'
# title = 'Interview invitation'
# content = 'Congratulations, after the interview, please come to work'
# smtp_server = 'smtp.126.com'
# port = 25
# mail = SendEmail()
# mail.send_email(title, from_email, to_email,pwd, content, smtp_server, port, excel_path, excel_name, jpg_path, jpg_name)

re_test = InterfaceTest()
# url="http://mt.youmeishi.cn:82"
# uri="/api/memberType"
url = r"http://mt.youmeishi.cn:81"
#接口地址
uri = "/uaa/oauth/token"
params = {'firstusername':"xxx","password":"xxx", 'grant_type':'first_user','username':'xxx'}
headers = {'Content-Type':'application/x-www-form-urlencoded','Authorization':'Basic eW1zLTMtY3JtOnRyMmx4Tnl2RW0wQVRXajhhYVNH',
           'Accept':'application/json,text/plain,*/*'}
#请求类型
reqform = 'POST'
#数据类型
dataform = 'Form'
#检查点
checkpoint = "'error_code': 0"
# params=
# reqform=
# dataform=
# checkpoint=
# headers=
# i=
# sheet=
# num=
# name=
log=Log("test").get_log()
re_test.testrequest(url,uri,params,reqform,dataform,checkpoint,headers)