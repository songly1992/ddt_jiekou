# encoding=utf-8

import time

# 用例路径
case_path="F:\\python_Jiekou\\Auto\\case"
# 测试报告路径
report_path="F:\\python_Jiekou\\Auto\\report\\"+"%s_report.html"%time.strftime('%Y_%m_%d')
reportexcel_path="F:\\python_Jiekou\\Auto\\report\\"+"%s_result.xls"%time.strftime('%Y_%m_%d')

#excel测试报告设置
projectname = '接口'            #项目名称
interfaceVersion = '1.0.1'      #接口版本
tijiao_time = '2018 - 3 - 12'   #提测时间
ceshi_person = 'leg' #测试人
ceshi_time = '2018 - 4 - 13'    #测试时间
shenhename = 'hh'             #审核人

# Excel数据路径
Excel_path="F:\\python_Jiekou\\Auto\\data\\casedata.xls"
# 读取Excel数据第几张表
sheet_id=0

# 这个是日志保存本地的路径
log_path = "F:\\python_Jiekou\\Auto\\report"

#数据库连接

#超时时间
Interface_Time_Out=5000

#失败重试
Config_Try_Num=3