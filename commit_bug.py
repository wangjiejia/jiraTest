# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/5 11:33
@Auth ： jiejia
@File ：commit_bug.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# -*- coding: utf-8 -*-

import requests
import xlrd
from jira import JIRA
jira = JIRA(server='http://10.1.0.3:18080', basic_auth=("wangzhifen", "jhlt@wzf"))
#############查询所有的项目###############
print(jira.priorities())
print(jira.auth)
def search_projects():
    # 全部项目
    projects = jira.projects()
    print('打印出公司的项目信息')
    # 单个项目
    print('项目名称  项目关键字  项目负责人  项目组件')
    list = []
    for i in range(len(projects)):
        project = jira.project(projects[i])
        print('名称:', project.name, ',关键字:', project.key, ',负责人', project.lead, ',组件:', project.components)
# search_projects()
###############通过问题id,查询所有的问题##############
# 'WST-134'
def seach_issue():
    issue = jira.search_issues('WST')
    print(issue)
#####################创建issue#####################
######创建单个issue########
def create_sinissue(summary, description):
    issue_dict = {
        # key 是项目空间的关键字，将issue记录到此空间
        'project': {'key': 'WST'},
        'issuetype': {'name': 'Bug'},
        'summary': summary,
        'description': description,
        'priority': {'name': 'Medium'},
        'assignee': {'name': "wangzhifen"}
    }
    jira.create_issue(issue_dict)

print('########3')

############批量创建issue###########
def create_allissue():
    issue_list = [{
        'project': {'key': 'WST'},
        'issuetype': {'name': 'Bug'},
        'summary': '简要1',
        'description': '描述1',
    },
        {
            'project': {'key': 'WST'},
            'issuetype': {'name': 'Bug'},
            'summary': '简要2',
            'description': '描述2',
        }
    ]
    jira.create_issue(issue_list)


################修改问题############
def updata_issue():
    issue = jira.issue('WST-135')
    issue_dict = {
        'summary': '新的概要',
        'description': '新的描述',
        'assignee': {'name': 'wangzhifen'}
    }
    issue.update(fields=issue_dict)


##################操作excel########################
class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    #############创建问题############
    def create_sinissue(self):
        #########得到项目的经办人###############
        # list1是为了显示的名字，list2是存用户名，方便建立问题。
        list1 = []
        list2 = []
        i = 2
        while i < 200:
            i = i + 1
            iss_id1 = "WST" + "-" + str(i)
            try:
                issue = jira.issue(iss_id1)
                name1 = (((issue.raw)['fields'])['assignee'])['displayName']
                list1.append(name1)
                name2 = (((issue.raw)['fields'])['assignee'])['name']
                list2.append(name2)
            except:
                pass
        ############去重,变成一个有序且不重复的元素集合######
        # 得到经办人的显示名字
        new_list1 = []
        for i in list1:
            if i not in new_list1:
                new_list1.append(i)
        # 得到经办人的用户名
        new_list2 = []
        for i in list2:
            if i not in new_list2:
                new_list2.append(i)
        if self.rowNum <= 1:
            print("测试用例总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}  #
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
                ##如果分配在文档里的话，直接创建问题,没有的话就为空
                for m in range(0, len(new_list1)):
                    if ((r[i]['assign'] == new_list1[m])):
                        assign_name = new_list2[m]
                    else:
                        assign_name = None
                issue_dict = {
                    # key 是项目空间的关键字，将issue记录到此空间
                    'project': {'key': 'WST'},
                    'issuetype': {'name': 'Bug'},
                    'summary': r[i]['summary'],
                    'description': r[i]['description'],
                    'priority': {'name': 'Medium'},
                    'assignee': {'name': assign_name}
                }
                jira.create_issue(issue_dict)
    ##############创建问题################


if __name__ == "__main__":
    filepath = r"C:\Users\HP\Desktop\jira_test.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    data.create_sinissue()





















