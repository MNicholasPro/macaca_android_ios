#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 15:54
# @Author  : zhoumingkai
# @Site    : 
# @File    : macaca_server.py
# @Software: PyCharm

import threading
import os


class RunServer(threading.Thread):
    '''
    重写子类方法run
    启动macaca服务，并加入线程中
    '''
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.cmd = 'macaca server -p %s --verbose' % port

    def run(self):
        os.system(self.cmd)