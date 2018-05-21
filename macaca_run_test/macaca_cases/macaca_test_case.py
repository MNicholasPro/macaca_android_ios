#coding:utf-8

import time


def case_login(driver):
    """
    这里运行你的测试用例, 在测试用例中driver可以通过以下方式获取
    """
    driver \
        .elements_by_class_name('android.widget.EditText')[0] \
        .send_keys('中文+Test+12345678')

    driver \
        .elements_by_class_name('android.widget.EditText')[1] \
        .send_keys('111111')

    time.sleep(1)
    # self.driver.keys(Keys.ENTER.value + Keys.ESCAPE.value)

    driver \
        .element_by_name('Login') \
        .click()

    driver \
        .wait_for_element_by_name('HOME') \
        .click()

    driver \
        .wait_for_element_by_name('list') \
        .click()

    time.sleep(2)

    driver \
        .wait_for_element_by_name('Alert') \
        .click()

    time.sleep(5)

    driver \
        .accept_alert()

    time.sleep(3)

    driver \
        .back()

    time.sleep(3)

    driver \
        .wait_for_element_by_name('Gesture') \
        .click()

    time.sleep(3)

    driver \
        .touch('tap', {
        'x': 100,
        'y': 100
    })

    time.sleep(5)

    driver \
        .touch('doubleTap', {
        'x': 100,
        'y': 100
    })

    time.sleep(5)

    driver \
        .touch('press', {
        'x': 100,
        'y': 100,
        'steps': 100
    })

    time.sleep(5)

    driver \
        .touch('drag', {
        'fromX': 100,
        'fromY': 100,
        'toX': 100,
        'toY': 600,
        'steps': 100
    })

    time.sleep(5)

    driver.back()

    time.sleep(5)

    driver.back()

    time.sleep(5)

    driver.quick()

