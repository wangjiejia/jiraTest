# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/5 10:16
@Auth ： jiejia
@File ：loginjira.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from jira import JIRA
import requests
def login():
    list1=[
        {
            "self": "http://pm.mianchao-inc.com/rest/api/2/user?username=wangjiejia",
            "key": "wangjiejia",
            "name": "wangjiejia",
            "emailAddress": "wangjiejia@mianchao-inc.com",
            "avatarUrls": {
                "48x48": "https://www.gravatar.com/avatar/86d5c391885eaa3db7d2c6db7831f512?d=mm&s=48",
                "24x24": "https://www.gravatar.com/avatar/86d5c391885eaa3db7d2c6db7831f512?d=mm&s=24",
                "16x16": "https://www.gravatar.com/avatar/86d5c391885eaa3db7d2c6db7831f512?d=mm&s=16",
                "32x32": "https://www.gravatar.com/avatar/86d5c391885eaa3db7d2c6db7831f512?d=mm&s=32"
            },
            "displayName": "王杰佳",
            "active": '',
            "timeZone": "Asia/Shanghai",
            "locale": "zh_CN"
        }
    ]
    print((list1[0])['name'])


login()
