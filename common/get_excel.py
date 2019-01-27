# -*- coding: utf-8 -*-

import xlrd,xlwt
import unittest,sys
# from xlutils.copy import copy
# from Interface.test_requests import requ
from config.config_set import Excel_path,sheet_id
from common.log import Log
log=Log()
log.info('解析测试用例文件')
def datacel():
    try:
        filepath=Excel_path
        file=xlrd.open_workbook(filepath)
        tables=file.sheets()[sheet_id]
        nrows=tables.nrows
        listid=[]
        listname=[]
        listurl=[]
        listrun=[]
        listmethond=[]
        listheader=[]
        listcase_depend=[]
        listdata_depend=[]
        listfield_depend=[]
        listdata_type=[]
        listdata=[]
        listexpect=[]
        for i in range(1,nrows):
            listid.append(tables.cell(i,0).value)
            listname.append(tables.cell(i,1).value)
            listurl.append(tables.cell(i,2).value)
            listrun.append(tables.cell(i,3).value)
            listmethond.append(tables.cell(i,4).value)
            listheader.append((tables.cell(i,5).value))
            listcase_depend.append((tables.cell(i,6).value))
            listdata_depend.append((tables.cell(i, 7).value))
            listfield_depend.append((tables.cell(i, 8).value))
            listdata_type.append((tables.cell(i, 9).value))
            listdata.append((tables.cell(i, 10).value))
            listexpect.append((tables.cell(i, 11).value))
        return listid,listname,listurl,listrun,listmethond,listheader,listcase_depend,listdata_depend,listfield_depend,listdata_type,listdata,listexpect
    except:
        log.info('打开测试用例失败，原因是:%s'%Exception)
log.info('生成数据驱动所用数据')
def makedata():
    listid, listname, listurl, listrun, listmethond, listheader, listcase_depend, listdata_depend, listfield_depend,listdata_type, listdata, listexpect=datacel()
    i=0
    make_data=[]
    for i in range(len(listid)):
        make_data.append({'id':listid[i],'name':listname[i],'url':listurl[i],'run':listrun[i],'methond':listmethond[i],'header':listheader[i],'case_depend':listcase_depend[i],'data_depend':listdata_depend[i],'field_depend':listfield_depend[i],'data_type':listdata_type[i],'data':listdata[i],'expect':listexpect[i]})
        i+=1
    return make_data

if __name__=="__main__":
    r=datacel()
    print(r)
    t=makedata()
    print(t)
    print(type(t))



