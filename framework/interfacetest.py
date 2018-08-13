# coding=utf-8
__author__ = 'tyr'
import sys
sys.path.append("E:\PythonFile\InterfaceTest\com\tyr\common")
from framework.interface_request import InterfaceRequest
import re


class InterfaceTest(object):
    def testrequest(self, url, uri, params, reqform ,dataform ,checkpoint ,headers):
        req = InterfaceRequest()
        full_url = url + uri
        if(reqform == 'GET'):
            self.req_test = req.req_get(full_url, params, headers)
        elif(reqform == 'POST' and dataform == 'Form'):
            self.req_test = req.post_kv(full_url, params, headers)
        elif(reqform == 'POST' and dataform == 'Json'):
            headers = {'Content-Type':'application/json;charset=utf-8'}
            self.req_test = req.post_json(full_url, params, headers)
        else:
            print("请求不通过，请检查case用例配置")
        print(self.req_test)
        #检查点与响应数据做对比
        # if(re.search(checkpoint,str(self.req_test))):
        #     sheet.cell(row=i, column=9).value = "成功"
        #     sheet.cell(row=i, column=11).value = str(self.req_test)
        #     log.info("用例编号"+str(num)+" "+name + "接口执行成功")
        # else:
        #     sheet.cell(row=i, column=9).value = "失败"
        #     sheet.cell(row=i, column=11).value = str(self.req_test)
        #     log.info("用例编号" + str(num) + " " + name + "接口执行失败")