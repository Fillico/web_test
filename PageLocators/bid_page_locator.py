#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/23
# description:

from selenium.webdriver.common.by import By


class BidPageLocator:
    # 投标输入框
    invest_input_loc = (By.CSS_SELECTOR, '.form-control')

    # 投标按钮
    invest_btn_loc = (By.XPATH, '//div[@class="pd-right"]//button')

    # 标剩余可投金额
    bid_last_loc = (By.CSS_SELECTOR, '.mo_span4')

    # 投标成功弹出框
    bid_success_alert = (By.XPATH, '//div[@class="layui-layer-content"]')

    # 投标弹出框-查看并激活按钮
    bid_success_look_btn = (By.XPATH, '//div[@class="layui-layer-content"]//button[text()="查看并激活"]')

    # 投标成功弹出框关闭按钮
    bid_success_alert_close = (By.XPATH, '//div[text()="投标成功！"]/preceding-sibling::div/img')

    # 投标失败弹出框
    bid_fail_alert = (By.CSS_SELECTOR,'.layui-layer')

    # 投标失败弹出框上的提示文字
    bid_fail_alert_msg = (By.CSS_SELECTOR, '.layui-layer-content>div')