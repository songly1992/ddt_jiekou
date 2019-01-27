# encoding=utf-8

import unittest
import ddt

from common.requets_case import Api
from common.get_excel import makedata
from common.log import Log
from common.send_email import SendEmail
from common.assertion import Assertion
from common.pyreport_excel import create
from config.config_set import Config_Try_Num
from common.data_deal import datatype_deal


data_test = makedata()
list_pass = []
list_fail = []
listids = []
listnames = []
listurls = []
listmatonds = []
listdatas = []
listexpects = []
list_json = []
listspends = []
listresult = []




@ddt.ddt
class MyTest(unittest.TestCase):

    def setUp(self):
        Log().info('------------测试用例开始执行-------------')
        print('------------测试用例开始执行-------------')


    @ddt.data(*data_test)    
    def test_case(self, data_test):
        self.send_email = SendEmail()
        self.assertion=Assertion()
        is_run=data_test['run']
        if is_run=='yes'or is_run=='YES':
            data=datatype_deal(data_test['data_type'],data_test['data'])#转换为字典类型
            testapi= Api(data_test['url'],data_test['methond'],data,data_test['header'])
            Log().info('请求传入数据：url:%s,请求方式:%s,参数:%s,期望结果：%s' % (data_test['url'], data_test['methond'],data_test['data'], data_test['expect']))
            apijson =testapi.getJson()
            spend = testapi.spend()
            listids.append(data_test['id'])
            listnames.append(data_test['name'])
            listurls.append(data_test['url'])
            listmatonds.append(data_test['methond'])
            listdatas.append(data_test['data'])
            listexpects.append(data_test['expect'])
            if self.assertion.is_contain(data_test['expect'],apijson):
                # self..write_result(data_test['result'], "pass")
                Log().info('------用例测试通过,实际结果：%s,响应时间：%s' % (apijson,spend))
                print('------用例测试通过,实际结果：%s,响应时间：%s' % (apijson,spend))
                # 统计通过的用例数
                list_pass.append('pass')
                listresult.append('pass')

            else:
                error_num=0
                for i in range(0,Config_Try_Num+10):
                     print(i)
                     if error_num<Config_Try_Num:
                        error_num+=1
                        Log().info('------>>失败重试第%s次'%error_num)
                        apijson = testapi.getJson()
                        spend = testapi.spend()
                        if self.assertion.is_contain(data_test['expect'], apijson):
                            Log().info('------用例测试通过,实际结果：%s,响应时间：%s' % (apijson, spend))
                            print('------用例测试通过,实际结果：%s,响应时间：%s' % (apijson, spend))
                            list_pass.append('pass')
                            listresult.append('pass')
                            break
                        else:
                            Log().info('------失败重试返回结果：%s' % apijson)
                     else:
                        Log().info('------失败重试中次数用完,用例测试失败，返回结果：%s' % apijson)
                        print('------失败重试中次数用完,用例测试失败，返回结果：%s' % apijson)
                        # 统计失败的用例数
                        list_fail.append('pail')
                        listresult.append('fail')
                        break
            list_json.append(apijson)
            listspends.append(spend)
            Log().info('------------测试用例执行完毕-------------')
            print('------------测试用例执行完毕-------------')



    @classmethod
    def tearDownClass(cls):
        pass_count=len(list_pass)
        fail_count=len(list_fail)
        Log().info('所有用例执行完成，成功数:%s,失败数：%s' % (pass_count, fail_count))
        print('所有用例执行完成，成功数:%s,失败数：%s' % (pass_count, fail_count))
        create(pass_count, fail_count, listids, listnames, listurls, listmatonds, listdatas, listexpects, list_json,listspends, listresult)
        #发送邮件
        # self.send_email.send_main(list_pass,list_fail)

if __name__ == "__main__":
    unittest.main()
