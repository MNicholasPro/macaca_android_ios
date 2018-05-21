#coding:utf-8

import unittest
import time
from macaca import WebDriver
from retrying import retry

desired_caps = {
    'platformName': 'android',
    'package':'com.tencent.mm',
    'activity':'.ui.LauncherUI'
    }

server_url = {
    'hostname': 'localhost',
    'port': 3456
}


class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.initDriver()

    @classmethod
    @retry
    def initDriver(cls):
        print("Retry connecting server...")
        cls.driver.init()

    def test_01_login(self):
        # 确认弹窗
        self.driver.accept_alert()

        # 确认弹窗
        self.driver.accept_alert()

        # 登录
        self.driver.elements_by_id('com.tencent.mm:id/d1w')[0].click()

        # 微信号/QQ号/邮箱登录
        self.driver.elements_by_id('com.tencent.mm:id/bwm')[0].click()

        # 输入账号
        self.driver.elements_by_class_name('android.widget.EditText')[0].send_keys('1319134962')

        # 输入密码
        self.driver.elements_by_class_name('android.widget.EditText')[1].send_keys('zz11mm33kk55hjcz')

        # 登录
        self.driver.elements_by_id('com.tencent.mm:id/bwn')[0].click()

        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()