# encoding: utf-8
"""
Excel测试报告
"""
from config.config_set import reportexcel_path
import xlrd ,os,xlwt#导入库
from xlwt import *
from config.config_set import projectname,interfaceVersion,tijiao_time,ceshi_person,ceshi_time,shenhename

def yangshi1():
    style = XFStyle()
    fnt = Font()
    fnt.name = u'微软雅黑'
    fnt.bold = True
    style.font = fnt
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment  # 给样式添加文字居中属性
    style.font.height = 430  # 设置字体大小
    return style
def yangshi2():
    style1 = XFStyle()
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style1.alignment = alignment  # 给样式添加文字居中属性
    style1.font.height = 330  # 设置字体大小
    return style1
def yangshi3():
    style1 = XFStyle()
    style1.font.height = 330  # 设置字体大小
    return style1
def yangshique(me):
    if me =='pass':
        style=yangshi1()
        Pattern=xlwt.Pattern()
        Pattern.pattern=xlwt.Pattern.SOLID_PATTERN
        Pattern.pattern_fore_colour=xlwt.Style.colour_map['green']
        style.pattern=Pattern
    else :
        style=yangshi2()
        Pattern=xlwt.Pattern()
        Pattern.pattern=xlwt.Pattern.SOLID_PATTERN
        Pattern.pattern_fore_colour=xlwt.Style.colour_map['red']
        style.pattern=Pattern
    return style
#生成测试报告
def create(list_pass,list_fail,listids,listnames,listurls,listmatonds,listdatas,listexpects,list_json,listspends,listrelust):
    file = Workbook(reportexcel_path)
    table = file.add_sheet('测试结果',cell_overwrite_ok=True)
    style=yangshi1()
    for i in range(0, 6):
        table.col(i).width = 380*20
    style1=yangshi2()
    table.write_merge(0,0,0,6,'测试报告',style=style)
    table.write_merge(1,1,0,6,'',style=style)
    table.write_merge(2,3,0,6,'测试详情',style=style1)
    table.write(4,0,'项目名称',style=style1)
    table.write(5,0,'接口版本',style=style1)
    table.write(6,0,'提测时间',style=style1)
    table.write(4,2,'测试人',style=style1)
    table.write(5,2,'测试时间',style=style1)
    table.write(6,2,'审核人',style=style1)
    table.write(4,4,'通过',style=style1)
    table.write(5,4,'失败',style=style1)
    table.write(6,4,'成功率',style=style1)
    table.write(4, 1, projectname,style=style1)
    table.write(5, 1, interfaceVersion,style=style1)
    table.write(6, 1, tijiao_time,style=style1)
    table.write(4, 3, ceshi_person,style=style1)
    table.write(5, 3, ceshi_time,style=style1)
    table.write(6, 3, shenhename,style=style1)
    table.write(4, 5, (list_pass), style=style1)
    table.write(5, 5, (list_fail), style=style1)
    table.write(6, 5, ('%.2f%%'%((list_pass)/(len(listrelust)))), style=style1)
    table1 = file.add_sheet('测试详情',cell_overwrite_ok=True)
    table1.write_merge(0,0,0,8,'测试详情',style=style)
    for i in range(0, 8):
        table1.col(i).width = 400*20
    table1.write(1,0,'用例ID',style=yangshi3())
    table1.write(1,1,'用例名称',style=yangshi3())
    table1.write(1,2,'url',style=yangshi3())
    table1.write(1,3,'请求方式',style=yangshi3())
    table1.write(1,4,'请求参数',style=yangshi3())
    table1.write(1,5,'预期结果',style=yangshi3())
    table1.write(1,6,'实际返回',style=yangshi3())
    table1.write(1,7,'响应时间(秒)',style=yangshi3())
    table1.write(1,8,'结果',style=yangshi3())
    for i in range(len(listids)):
        table1.write(i+2, 0, listids[i],style=yangshi3())
        table1.write(i+2, 1, listnames[i],style=yangshi3())
        table1.write(i+2, 2, listurls[i],style=yangshi3())
        table1.write(i+2, 3, listmatonds[i],style=yangshi3())
        table1.write(i+2, 4, listdatas[i],style=yangshi3())
        table1.write(i+2, 5, listexpects[i],style=yangshi3())
        table1.write(i+2, 6, str(list_json[i]),style=yangshi3())
        table1.write(i+2, 7, listspends[i],style=yangshi3())
        table1.write(i+2, 8, listrelust[i], style=yangshique(listrelust[i]))
    file.save(reportexcel_path)

if __name__=="__main__":
    list_pass=1
    list_fail=3
    listids=['f4',"f4"]
    listnames=['f7',"f7"]
    listurls=['f7',"f7"]
    listmatonds=['f7',"f7"]
    listdatas=['f7',"f7"]
    listexpects=['f7',"f7"]
    list_json=['f7',"f7"]
    listspends=['f7',"f7"]
    listrelust=['f7',"f7"]
    create(list_pass, list_fail, listids, listnames, listurls, listmatonds, listdatas, listexpects, list_json,
           listspends, listrelust)