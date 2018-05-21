#coding:utf-8

import unittest
import os
import time
from macaca import WebDriver
from macaca import Keys
from retrying import retry

desired_caps = {
    'platformName': 'android',
    'app': 'https://npmcdn.com/android-app-bootstrap@latest/android_app_bootstrap/build/outputs/apk/android_app_bootstrap-debug.apk',
    }

server_url = {
    'hostname': 'localhost',
    'port': 3456
}

def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
    return driver

def switch_to_native(driver):
    contexts = driver.contexts
    driver.context = contexts[0]
    return driver

class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.initDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    @retry
    def initDriver(cls):
        print("Retry connecting server...")
        cls.driver.init()

    def test_01_login(self):
        el = self.driver \
            .elements_by_class_name('android.widget.EditText')[0] \
            .send_keys('中文+Test+12345678')   \

        el = self.driver \
            .elements_by_class_name('android.widget.EditText')[1] \
            .send_keys('111111')

        time.sleep(1)
        # self.driver.keys(Keys.ENTER.value + Keys.ESCAPE.value)

        self.driver \
            .element_by_name('Login') \
            .click()

if __name__ == '__main__':
    unittest.main()