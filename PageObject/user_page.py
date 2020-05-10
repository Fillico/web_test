#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/23
# description:

from Common.basepage import BasePage

from PageLocators.user_page_locator import UserPageLocator as loc


class UserPage(BasePage):

    def get_user_left_money(self):
        # self.driver.get(cd.user_center_url)
        self.wait_eleVisible(loc.left_money_loc,"个人中心_获取用户剩余金额")
        text = self.get_element_text(loc.left_money_loc,"个人中心_获取用户剩余金额")
        return text.strip("元")

