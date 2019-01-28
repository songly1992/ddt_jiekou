# encoding=utf-8
import json
'''
数据类型处理
参数数据填写统一为json格式
post传递参数的类型：application/x-www-form-urlencoded ，text/xml，参数类型为data,应为dict
post传递参数的类型：application/json ，参数类型为json，应为str
'''
def datatype_deal(datatype,data):
    if datatype=='data':
        if isinstance(data,str):
            data=json.loads(data)
    else:
        data = data
    return data

#处理header，若为空不处理,若不为空，转换为字典类型
def header_deal(header):
    if header !="":
        if isinstance(header,str):
           header=json.loads(header)
    else:
        header=header
    return header

