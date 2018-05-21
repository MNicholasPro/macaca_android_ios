#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 17:26
# @Author  : zhoumingkai
# @Site    : 
# @File    : macaca_run_1_copy.py
# @Software: PyCharm

import os
import requests
from requests.exceptions import ConnectionError
from requests.exceptions import ReadTimeout
from multiprocessing.pool import Pool
from time import sleep
from macaca import WebDriver
from macaca_driver import DRIVER
from macaca_test_before import InitDevice
from macaca_port import get_port
from macaca_server import RunServer
from macaca_cases.macaca_alltests import run_test


class MacacaServer():
    def __init__(self):
        i = InitDevice()
        self.devices = i.get_device()
        self.count = len(self.devices)
        self.url = 'http://127.0.0.1:%s/wd/hub/status'

    def is_running(self, port):
        """Determine whether server is running
        :return:True or False
        """
        url = self.url % port
        response = None
        try:
            response = requests.get(url, timeout=0.01)
            if str(response.status_code).startswith('2'):
                return True
            return False
        except ConnectionError:
            return False
        except ReadTimeout:
            return False
        finally:
            if response:
                response.close()


    def run_server(self, device, port):
        r = RunServer(port)
        r.start()
        while not self.is_running(port):
            sleep(1)
        server_url = {
            'hostname': "localhost",
            'port': port,
        }
        driver = WebDriver(device, server_url)
        driver.init()
        DRIVER.set_driver(driver)
        DRIVER.set_OS(device.get("platformName"))
        driver = DRIVER.driver
        run_test(driver)

    def run(self):
        if self.count == 0:
            print("Have no device!")
            return
        pool = Pool(processes=self.count)
        port_list = get_port(self.count)
        for i in range(self.count):
            pool.apply_async(self.run_server, args=(self.devices[i], port_list[i]))
            sleep(3)
        pool.close()
        pool.join()

        sleep(8)
        KILL_NODE = "killall -9 node"
        os.popen(KILL_NODE)

if __name__ == "__main__":

    m = MacacaServer()
    m.run()