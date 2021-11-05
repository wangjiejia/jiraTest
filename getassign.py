# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/4 15:10
@Auth ： jiejia
@File ：getjira.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# coding:utf-8
import requests
from jira import JIRA
import xlsxwriter
###获取jira
def getassign():
    # jira访问地址
    # server = 'http://pm.mianchao-inc.com/login.jsp'
    # 用户名密码以元祖的方式传递。uesrname、passwd填写真实的账号密码
    jr = JIRA(server="http://pm.mianchao-inc.com", basic_auth=('wangjiejia', 'wangjiejia'))
    # jrproject=jr.projects()
    # print(" ".join(str(i) for i in (jrproject)))
    old_list = []
    i = 2
    while i < 7:
        i = i + 1
        iss_id = "YFB" + "-" + str(i)
        try:
            issue = jr.issue(iss_id)
            name = (((issue.raw)['fields'])['assignee'])['displayName']
            old_list.append(name)
        except:
            pass
    # print(old_list[0])
    # print(old_list)
    # print(set(old_list))
#循环遍历，将原来的列表中的元素去重
    new_list=[]
    for i in old_list:
        if i in new_list:
            continue
        new_list.append(i)
    # print(new_list)
    num=len(new_list)
    # print(num)
    i = 0
    if i < num+1:
        name = new_list[i]
        print(name)


def create_exel():
    workbook = xlsxwriter.Workbook('bug.xlsx') #建立文件
    workbook = workbook.add_worksheet()
    workbook.write('A1','hello world')
    workbook.close()
        #
        # worksheet = workbook.add_worksheet()  # 建立sheet， 可以work.add_worksheet('employee')来指定sheet名，但中文名会报UnicodeDecodeErro的错误
        # worksheet.write('A1', 'Hello world')  # 向A1写入
        # worksheet.write(1, 1, 'guoshun')  # 向第二行第二例写入guoshun
        # workbook.close()

getassign()

