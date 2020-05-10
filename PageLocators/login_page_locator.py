#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/23
# description:

from selenium.webdriver.common.by import By

class LoginPageLocator:
    # 用户名输入框
    user_loc = (By.CSS_SELECTOR,'.username')
    # 密码输入框
    passwd_loc = (By.NAME,'password')
    # 登录按钮
    login_button_loc = (By.TAG_NAME,'button')
    # 提示框 - 登录表单提示框
    error_msg_from_loginForm = (By.CSS_SELECTOR,'.form-error-info')
    # 提示框 - 页面中间区域
    error_notify_from_pageCenter = (By.CSS_SELECTOR,'.layui-layer-content')