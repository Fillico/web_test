#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/29
# description:

# 记录用例执行过程 - 日志
# 如果用例失败了 - Trackback报错信息\失败截图
# 记录一下用例的运行时间 - 起始 - 等待的时候 - 等待的时长

# 用例、页面对象当中。 用例 = 页面对象 +　测试数据
# 断言失败了！页面对象方法执行的时候，报错了

import HTMLTestRunnerNew
# 测试报告
import unittest

# from web_login.TestCases
from Common.dir_config import *

suite = unittest.TestSuite()
loader = unittest.TestLoader()

# discover = unittest.defaultTestLoader()
suite.addTests(loader.discover(testcases_dir))

html_file = htmlreport_dir+'/autoTest_report.html'

with open(html_file,'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title="ui自动化测试报告",
        tester="Fillico")
    runner.run(suite)

# pytest --html=report.html