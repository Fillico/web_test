#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/22
# description:登录的测试数据

from TestDatas.common_datas import base_url

success_data = {"user": "18684720553", "password": "python",
                "check": "{}Index/index".format(base_url)}

# 用户名为空/密码为空/用户名格式不正确......
wrong_datas = [
    {"user": "", "password": "python", "check": "请输入手机号"},
    {"user": "18684720553", "password": "", "check": "请输入密码"},
    {"user": "186847205531", "password": "python", "check": "请输入正确的手机号"},
    {"user": "1868472055", "password": "python", "check": "请输入正确的手机号"},
    {"user": "1868472 0553", "password": "python", "check": "请输入正确的手机号"},
    {"user": "186847aa553", "password": "python", "check": "请输入正确的手机号"}
]

fail_datas = [
    {"user": "13200000000", "password": "python", "check": "此账号没有经过授权，请联系管理员!"},
    {"user": "18684720553", "password": "123456", "check": "帐号或密码错误!"}
]
