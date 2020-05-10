#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/29
# description:

import pytest
from PageObject.login_page import LoginPage
from TestDatas import login_datas as ld

from PageObject.index_page import IndexPage


# pytestmark = pytest.mark.module # 模块级别的标签名   放在引入包的后面，所有用例的前面

# @pytest.mark.login  # 整个TestLogin类里面，所有测试用例都有login标签
@pytest.mark.usefixtures("open_url")  # 使用函数名称为open_url的fixture
@pytest.mark.usefixtures("refresh_page")
class TestLoginP:
    pytestmark = pytest.mark.login

    @pytest.mark.parametrize("data", ld.wrong_datas)
    def test_login_0_failed_by_wrong_datas(self, data, open_url):  # 手机号为空
        LoginPage(open_url).login(data["user"], data["password"])
        assert data["check"] == LoginPage(open_url).get_error_msg_from_loginForm()

    @pytest.mark.parametrize("data", ld.fail_datas)
    def test_login_1_failed_by_fail_datas(self, data, open_url):
        LoginPage(open_url).login(data["user"], data["password"])
        assert data["check"] == LoginPage(open_url).get_error_msg_from_pageCenter()

    @pytest.mark.smoke
    def test_login_success(self, open_url):  # open_url = driver
        LoginPage(open_url).login(ld.success_data["user"], ld.success_data["password"])
        assert IndexPage(open_url).check_nick_name_exists()
        # url跳转，比对当前的url结果和实际结果
        assert open_url.current_url == ld.success_data["check"]

        # 异常用例 - 读取test_cases里面的wrong_datas


class TestTT:
    pytestmark = pytest.mark.demo

    def test_add(self):
        c = 100 + 200
        assert c == 300

    def test_demo(self):
        print("dem------")
