#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:Fillico
# date:2019/6/27
# description:

import datetime
import logging
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Common.dir_config import screenshot_dir


class BasePage:
    # 包含了PageObjects当中，用到所有的selenium底层方法
    # 还可以包含通用的一些元素操作，如alert,iframe,windows...
    # 还可以自己额外封装一些web相关的断言
    # 实现日志记录，实现失败截图

    def __init__(self, driver):
        self.driver = driver

    def wait_eleVisible(self, loc, img_doc, timeout=30, frequency=0.5):
        logging.info("等待元素 {} 可见".format(loc))
        try:
            # 起始等待的时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
            # 结束等待的时间
            end = datetime.datetime.now()
            logging.info("开始等待时间点：{},结束等待时间点：{}，等待时长为：{}".format(start, end, end - start))
        except:
            # 日志
            logging.exception("等待元素可见失败")
            # 截图 - 哪一个页面哪一个操作导致的失败，+ 当前时间
            self.save_web_screenshot(img_doc)
            raise

    def get_element(self, loc, img_doc=""):
        logging.info("查找 {} 中的元素 {}".format(img_doc, loc))
        try:
            ele = self.driver.find_element(*loc)
            return ele
        except:
            # 日志
            logging.exception("查找元素失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    def click_element(self,loc, img_doc, timeout=30, frequency=0.5):

        self.wait_eleVisible(loc, img_doc, timeout, frequency)
        ele = self.get_element(loc, img_doc)
        logging.info("点击元素：{}".format(loc))
        try:
            ele.click()
        except:
            logging.exception("点击元素失败")
            self.save_web_screenshot(img_doc)
            raise

    def input_text(self,loc,img_doc,*args):
        self.wait_eleVisible(loc,img_doc)
        ele = self.get_element(loc,img_doc)
        logging.info("给元素 {} 输入文本内容：{}".format(loc,args))
        try:
            ele.send_keys(*args)
        except:
            logging.exception("元素输入操作失败")
            self.save_web_screenshot(img_doc)
            raise


    def get_element_attribute(self,loc,attr_name,img_doc):
        ele = self.get_element(loc,img_doc)
        try:
            attr_value = ele.get_attribute(attr_name)
            logging.info("获取元素 {} 的属性 {} 值为：{}".format(loc,attr_name,attr_value))
            return attr_value
        except:
            logging.exception("获取元素属性失败")
            self.save_web_screenshot(img_doc)
            raise

    def get_element_text(self,loc,img_doc):
        ele = self.get_element(loc,img_doc)
        try:
            text = ele.text
            logging.info("获取元素 {} 的文件值为 {}".format(loc,text))
            return text
        except:
            #日志
            logging.exception("获取元素文本值失败")
            self.save_web_screenshot(loc,img_doc)
            raise


    # 实现网页截图操作
    def save_web_screenshot(self, img_doc):
        # 页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filepath = "{}_{}.png".format(img_doc, now)
        try:
            self.driver.save_screenshot(screenshot_dir + "/" + filepath)
            logging.info("网页截图成功。图片存储在:{}".format(screenshot_dir + "/" + filepath))
        except:
            logging.exception("网页截屏失败")

    # windows切换
    def switch_window(self):
        pass

    # iframe切换
    def switch_iframe(self, iframe_reference):
        # 等待可用的iframe并切换 -webDriverWait
        pass

    # select下拉列表

    # 上传操作
