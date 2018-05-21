#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 15:57
# @Author  : zhoumingkai
# @Site    : 
# @File    : macaca_alltests.py
# @Software: PyCharm

from macaca_cases.macaca_test_case import case_login


def run_test(driver):
    """
    这里运行你的测试用例, 在测试用例中driver可以通过以下方式获取
    """
    case_login(driver)