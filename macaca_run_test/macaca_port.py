#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 15:53
# @Author  : zhoumingkai
# @Site    : 
# @File    : macaca_port.py
# @Software: PyCharm
import os


def is_using(port):
    """
    判断端口号是否被占用
    :param port:
    :return:
    """
    cmd = "netstat -an | grep %s" % port

    if os.popen(cmd).readlines():
        return True
    else:
        return False


def get_port(count):
    """
    获得3456端口后一系列free port
    :param count:
    :return:
    """
    port = 3456
    port_list = []
    while True:
        if len(port_list) == count:
            break

        if not is_using(port) and (port not in port_list):
            port_list.append(port)
        else:
            port += 1

    return port_list