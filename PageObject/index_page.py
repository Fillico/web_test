#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/7
# function:
import time

from PageLocators.index_page_locator import IndexPageLocator as loc

from Common.basepage import BasePage


class IndexPage(BasePage):
    # 检查昵称是否存在
    def check_nick_name_exists(self):
        """
        # 检查首页是否有“关于我们”
        :return:存在返回True,不存在返回False.
        """
        # WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located((By.XPATH, '//a[text()="关于我们"]')))
        # time.sleep(0.5)
        self.wait_eleVisible(loc.about_us_loc, "首页_关于我们")
        time.sleep(0.5)
        try:
            # self.driver.find_element_by_xpath('//a[contains(text(),"我的帐户")]')#一般不用这个，一般用首页的url判断
            self.get_element(loc.my_account_lin_loc, "首页_用户昵称")
            return True
        except:
            return False

    # 点击抢投标按钮(3个抢投标按钮)
    def click_invest_btn(self):
        self.wait_eleVisible(loc.invist_btns,"首页_等待抢投标按钮")
        self.click_element(loc.invist_btns, "首页_抢投标按钮")
