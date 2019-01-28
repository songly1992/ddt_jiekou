# -*- coding: utf-8 -*-
'''接口请求封装后的使用模块
调用类，传入url，请求方法，参数，请求headers，就可以进行请求，
目前只支持dict格式的参数，和请求headers。
'''
from common.requets_fenzhuang import Reques
import json

class Api():
   def __init__(self,url,methond,params,headers):
        self.url=url
        self.methond=methond
        self.param=params
        self.headers=headers
        self.requ=Reques()
        self.response=[]
   def testapi(self):
        global response,spend
        if self.methond=='POST' or self.methond=='post':
            response,spend=self.requ.post(url=self.url, params=self.param, headers=self.headers)
        elif self.methond=='GET' or self.methond=='get':
            response,spend=self.requ.get(url=self.url,params=self.param,headers=self.headers)
        elif self.methond=='PUT' or self.methond=='put':
            response,spend=self.requ.putfile(url=self.url,params=self.param,headers=self.headers)
        elif self.methond=='DELETE' or self.methond=='delete':
            response,spend=self.requ.delfile(url=self.url,params=self.param,headers=self.headers)
        return response,spend
   def getJson(self):
        json_data,spend=self.testapi()
        return json_data
   def spend(self):
        json_data, spend = self.testapi()
        return spend

if __name__=="__main__":
    url=r'http://120.79.232.23:8000/api/user/login'
    # data={"username":"13316588360","password":"sly1992.","verify":"","referer":"https://m.imooc.com"}
    data={'username':'admin','password':'admin369874125'}

    data=json.dumps(data)

    # headers=json.loads(headers)
    headers={"Content-Type":"application/json;charset=UTF-8"}
    r=Api(url,'post',data,headers)
    w=r.getJson()
    t=r.spend()
    print(headers)
    print("type%s" % type(headers))
    print(w)
    print(t)