# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/5 10:15
@Auth ： jiejia
@File ：commitBug.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from jira import JIRA
import xlsxwriter
import xlrd
import xlwt
def commit():
    work_book = xlwt.Workbook(encoding='utf-8')
    sheet = work_book.add_sheet('bugfix')
    sheet.write(0, 0, 'summary')
    sheet.write(0, 1, 'description')
    sheet.write(0, 2, 'assign')
    work_book.save('bug.xls')


commit()
