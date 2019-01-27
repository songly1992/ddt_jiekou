# -*- coding: utf-8 -*-
'''
判断预期结果与实际结果
'''
from common.log import Log
import json
import operator

class Assertion():

    def is_contain(self, str1, str2):
        '''
        判断一个字符串是否在另一个字符串中
        :param str1:
        :param str2:
        :return:
        '''
        flag = None
        if isinstance(str1, dict):
            str1 =json.dumps(str1)
        if str1 in str2:
            flag = True
        else:
            flag = False
        return flag
        # flag = None
        # if str1 in str2:
        #     flag = True
        # else:
        #     flag = False
        # return flag


    def is_equal_dict(self, dict_one, dict_two):
        '''
        判断两个字典是否相等
        '''
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        # return cmp(dict_one, dict_two) python2中使用
        return operator.eq(dict_one, dict_two)  # pyhon3中使用


