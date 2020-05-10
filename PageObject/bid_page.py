#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/23
# description:

from PageLocators.bid_page_locator import BidPageLocator as loc

from Common.basepage import BasePage


class BidPage(BasePage):
    # 投资
    def invest(self, money):
        self.input_text(loc.invest_input_loc, "标页面_投标输入框", money)
        self.click_element(loc.invest_btn_loc, "标页面_投标按钮")

    def get_user_left_money(self):
        self.wait_eleVisible(loc.invest_btn_loc, "标页面_投标输入框")
        self.get_element_attribute(loc.invest_btn_loc, "data-amount", "获取投标数额")

    def get_bid_money(self):
        bid_can_invest_money = self.get_element_text(loc.bid_last_loc, "标页面_剩余可投金额")
        return bid_can_invest_money

    # 获取投标按钮上面的文字
    def get_btn_text(self,money):
        self.input_text(loc.invest_input_loc, "标页面_投标输入框", money)
        self.wait_eleVisible(loc.invest_btn_loc, "标页面_投标按钮上错误提示")
        return self.get_element_text(loc.invest_btn_loc, "标页面_投标按钮上错误提示")

    # 投资成功的提示框 - 点击查看并激活
    def click_activeButton_on_success_popup(self):
        self.wait_eleVisible(loc.bid_success_alert, "标页面_投资成功提示框")
        self.click_element(loc.bid_success_look_btn, "标页面_投资成功提示框_点击查看并激活")

    # 获取失败弹出框上面的文字
    def get_fail_alert_text(self):
        self.wait_eleVisible(loc.bid_fail_alert,"标页面_投标失败弹出框")
        ele_alert = self.get_element_text(loc.bid_fail_alert_msg, "标页面_失败弹出框文字")
        return ele_alert
