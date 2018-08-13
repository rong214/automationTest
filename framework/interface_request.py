# coding=utf-8
__author__ = 'tyr'
import requests
import json
class InterfaceRequest(object):
    def req_get(self, url, params, headers):
        try:
            r = requests.get(url, params=params, headers=headers)
            json_r = r.json()
            return json_r
        except BaseException as e:
            print("请求不能完成：", str(e))

    def post_kv(self, url, data, headers):
        try:
            r = requests.post(url, data=data, headers=headers)
            json_r = r.json()
            return json_r
        except BaseException as e:
            print("请求不能完成：", str(e))

    def post_json(self, url, data, headers):
        try:
            data = json.dumps(data)
            r = requests.post(url, data=data, headers=headers)
            json_r = r.json()
            return json_r
        except Exception as e:
            print("请求不能完成：", str(e))
