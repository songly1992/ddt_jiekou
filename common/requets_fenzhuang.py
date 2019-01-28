# encoding=utf-8
'''
requets模块的简单的封装
'''
import requests,json
from config.config_set import Interface_Time_Out
from requests import exceptions
from common.log import Log
class Reques():

    def get(self,url,params,headers): #get消息
        try:
            if headers != None:
                self.r = requests.get(url=url,params=params, headers=headers, verify=False,timeout=Interface_Time_Out)
            else:
                self.r = requests.get(url=url,params=params, verify=False,timeout=Interface_Time_Out)
            print(self.r.status_code)
            json_response = self.r.text.encode('utf-8').decode("unicode_escape")
            spend = self.r.elapsed.total_seconds()
            return json_response,spend
        except exceptions.Timeout:
            Log().error('get请求出错: 请求超时')
            return {'get请求出错': "请求超时"}
        except exceptions.InvalidURL:
            Log().error('get请求出错: 非法url')
            return {'get请求出错': "非法url"}
        except exceptions.HTTPError:
            Log().error('get请求出错: http请求错误')
            return {'get请求出错': "http请求错误"}
        except Exception as e:
            Log().error('get请求出错: 错误原因:%s' % e)
            return {'get请求出错':"错误原因:%s" % e}

    def post(self,url, params,headers):#post消息
        try:
            if headers != None:
                self.r = requests.post(url=url,data=params, headers=headers, verify=False,timeout=Interface_Time_Out)
            else:
                self.r = requests.post(url=url,data=params, verify=False,timeout=Interface_Time_Out)
            print(self.r.status_code)
            # json_response =self.r.text.encode('utf-8').decode("unicode_escape")
            json_response = self.r.text
            spend = self.r.elapsed.total_seconds()
            return json_response,spend
        except exceptions.Timeout:
            Log().error('get请求出错: 请求超时')
            return {'get请求出错': "请求超时"}
        except exceptions.InvalidURL:
            Log().error('get请求出错: 非法url')
            return {'get请求出错': "非法url"}
        except exceptions.HTTPError:
            Log().error('get请求出错: http请求错误')
            return {'get请求出错': "http请求错误"}
        except Exception as e:
            Log().error('get请求出错: 错误原因:%s' % e)
            return {'get请求出错': "错误原因:%s" % e}

    def delfile(self,url,params,headers):#删除的请求
        try:
            self.rdel_word=requests.delete(url,data=params,headers=headers,timeout=Interface_Time_Out)
            json_response=self.rdel_word.text.encode("utf-8").decode("unicode_escape")
            spend=self.rdel_word.elapsed.total_seconds()
            return json_response,spend
        except exceptions.Timeout:
            Log().error('get请求出错: 请求超时')
            return {'get请求出错': "请求超时"}
        except exceptions.InvalidURL:
            Log().error('get请求出错: 非法url')
            return {'get请求出错': "非法url"}
        except exceptions.HTTPError:
            Log().error('get请求出错: http请求错误')
            return {'get请求出错': "http请求错误"}
        except Exception as e:
            Log().error('get请求出错: 错误原因:%s' % e)
            return {'get请求出错': "错误原因:%s" % e}

    def putfile(self,url,params,headers):#put请求
        try:
            self.rdata=json.dumps(params)
            me=requests.put(url,self.rdata,headers=headers,timeout=Interface_Time_Out)
            json_response=json.loads(me.text)
            spend=me.elapsed.total_seconds()
            return json_response,spend
        except exceptions.Timeout:
            Log().error('get请求出错: 请求超时')
            return {'get请求出错': "请求超时"}
        except exceptions.InvalidURL:
            Log().error('get请求出错: 非法url')
            return {'get请求出错': "非法url"}
        except exceptions.HTTPError:
            Log().error('get请求出错: http请求错误')
            return {'get请求出错': "http请求错误"}
        except Exception as e:
            Log().error('get请求出错: 错误原因:%s' % e)
            return {'get请求出错': "错误原因:%s" % e}

if __name__=="__main__":
    url = r'http://m.imooc.com/'

    data={""}

    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://m.imooc.com/passport/user/login",
        # "Cookie":  # 头部没登录前不用传cookie，因为这里cookie就是保持登录的
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        }
    # r = Reques()
    # print type(data)
    # print(type(data))
    # re1 = r.post(url,data)
    print(type(data))
    r = requests.post(url=url, params=data, headers=headers, verify=False, timeout=Interface_Time_Out)
    w = r.text.encode('utf-8').decode("unicode_escape")
    print("get请求获取响应头", r.headers['Content-Type'])
    print("cookies:",r.cookies)
    # print(type(data))
    # w,t= r.post(url,data,headers)
    print("type%s" % type(w))
    print(w)
    # print(t)


