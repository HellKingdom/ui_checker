# !/usr/bin/env python
# -*- coding=utf-8 -*-

from time import sleep
from page.page import BasePage
from util.browser import Chrome


class FinishPage(BasePage):
    # page = __file__
    menu = ''
    subject = ''

    def do_something(self):
        pass



if __name__ == '__main__':
    d = Chrome.normal()
    # d = Chrome.headless()
    p = FinishPage(d)
    p.load()
    p.do_somthing()
    sleep(5)
    d.quit()