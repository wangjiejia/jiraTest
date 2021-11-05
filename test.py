# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/4 17:33
@Auth ： jiejia
@File ：test.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import numpy as np
from jira import JIRA
import requests
import loginjira
import re
import itertools


def search_user():
    jira = JIRA(server="http://pm.mianchao-inc.com", basic_auth=('wangjiejia', 'wangjiejia'))
    jrproject = jira.projects()
    # try:
    name1 = jira.search_assignable_users_for_projects('霍艳杰', 'CRM')
    print((name1[0]).name)
    # except:
    #     pass
search_user()
    # list1=["<",">"]
    # print(name1)
    # print((name1[0]))
    # print(len(name1))
    # coding=utf-8
    # 声明两个列表变量
    # list1 = ['Python', 'PHP', 'Java', 'Bash']
    # list2 = ['JavaScript是客户端脚本语言',
    #          'PHP是服务器端脚本语言',
    #          'Java是一种编程语言',
    #          'Kotlin是一种静态编程语言']
    #
    # # 根据第一个列表过滤第二个列表
    # filter_data = [x for x in list2 if
    #                all(y  in x for y in list1)]
    #
    # # 在过滤前和过滤后打印列表数据
    # print("第一个列表的内容:", list1)
    # print("第二个列表的内容:", list2)
    # print("过滤后的第二个列表的内容:", filter_data)







