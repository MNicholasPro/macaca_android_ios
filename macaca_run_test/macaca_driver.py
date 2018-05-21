#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 16:44
# @Author  : zhoumingkai
# @Site    : 
# @File    : macaca_drivers_copy.py
# @Software: PyCharm

class DRIVER:

    driver = None
    OS = None

    @classmethod
    def set_driver(self, driver):
        self.driver = driver

    @classmethod
    def set_OS(self, OS):
        self.OS = OS
