# encoding=utf-8

'''
数据类型处理
参数数据填写统一为json格式
post传递参数的类型：application/x-www-form-urlencoded ，text/xml，参数类型为data
post传递参数的类型：application/json ，参数类型为json
'''
def datatype_deal(datatype,data):
    if datatype=='data':
        if isinstance(data,str):
            data=eval(data)
    else:
        pass
    return data
