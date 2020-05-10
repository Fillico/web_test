#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/29
# description:

import pytest

if __name__ == '__main__':
    pytest.main(["-m","smoke","--alluredir=Outputs/allure_report"])

# 运行这个文件，或者在命令行运行命令 pytest -m smoke

# 1、allure命令行
# 2、pytest插件，