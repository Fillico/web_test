#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/27
# description:

import os

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir = os.path.join(base_dir,"TestDatas")

testcases_dir = os.path.join(base_dir,'TestCases')

htmlreport_dir = os.path.join(base_dir,"Outputs/reports")

logs_dir = os.path.join(base_dir,"Outputs\logs")

screenshot_dir = os.path.join(base_dir,"Outputs\screenshots")
print(screenshot_dir)
# print(base_dir)