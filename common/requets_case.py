# -*- coding: utf-8 -*-
'''接口请求封装后的使用模块
调用类，传入url，请求方法，参数，请求headers，就可以进行请求，
目前只支持dict格式的参数，和请求headers。
'''
from common.requets_fenzhuang import Reques

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
    url=r'http://m.imooc.com/passport/user/login'
    # data={"username":"13316588360","password":"sly1992.","verify":"","referer":"https://m.imooc.com"}
    data="username=13316588360&password=sly1992.&verify=&referer=https://m.imooc.com"
    headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Connection": "close"}
    r=Api(url,'post',data,headers)
    w=r.getJson()
    t=r.spend()
    print(data)
    print("type%s" % type(w))
    print(w)
    print(t)