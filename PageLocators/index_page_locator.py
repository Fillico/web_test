#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/23
# description:

from selenium.webdriver.common.by import By

class IndexPageLocator:

    # 关于我们
    about_us_loc = (By.XPATH, '//a[text()="关于我们"]')

    # 我的帐户链接
    my_account_lin_loc = (By.XPATH,'//a[@href="/Member/index.html"]')

    # 抢投标按钮(首页的3个抢投标按钮）
    # invist_btns = (By.CSS_SELECTOR,'.btn-special')
    invist_btns = (By.XPATH,'//a[@class="btn btn-special"]')
