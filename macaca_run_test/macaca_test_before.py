#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 15:37
# @Author  : zhoumingkai
# @Site    : 
# @File    : macaca_test_before.py
# @Software: PyCharm

import os
import re

'''
定义全局变量
'''
ANDROID_PACKAGE = "com.github.android_app_bootstrap"
ANDROID_ACTIVITY = ".activity.WelcomeActivity"
IOS_BUNDLE = "YOUR IOS BUNDLE ID"


class InitDevice():
    """
    获取连接的设备的信息
    """
    def __init__(self):
        self.GET_ANDROID = "adb devices"
        self.GET_IOS = "instruments -s devices"

    def get_device(self):
        device = []

        value = os.popen(self.GET_ANDROID)
        for v in value.readlines():
            android = {}
            s_value = str(v).replace("\n", "").replace("\t", "")
            if s_value.rfind('device') != -1 and (not s_value.startswith("List")) and s_value != "":
                android['platformName'] = 'Android'
                android['app'] = '/Users/april_chou/Downloads/android_app_bootstrap-debug.apk'
                android['udid'] = s_value[:s_value.find('device')].strip()
                android['package'] = ANDROID_PACKAGE
                android['activity'] = ANDROID_ACTIVITY
                device.append(android)

        value = os.popen(self.GET_IOS)
        for v in value.readlines():
            iOS = {}
            s_value = str(v).replace("\n", "").replace("\t", "").replace(" ", "")
            if v.rfind('Simulator') != -1:
                continue
            if v.rfind("(") == -1:
                continue
            iOS['platformName'] = 'iOS'
            iOS['platformVersion'] = re.compile(r'\((.*)\)').findall(s_value)[0]
            iOS['deviceName'] = re.compile(r'(.*)\(').findall(s_value)[0]
            iOS['udid'] = re.compile(r'\[(.*?)\]').findall(s_value)[0]
            iOS['bundleId'] = IOS_BUNDLE
            device.append(iOS)

        return device