import time
import requests
from Conf import *
from operation import Operation
from pprint import pprint
import random


def run_operation():
    #print('-1')
    op = Operation()
   # print('0')
    driver = op.driver

    #print('1')

    op.quit_frame()
    op.click('//a[text()="平台招商"]')
    time.sleep(2)
    download_tag_1 = '//div[@class="ant-spin-container"]/div/div/button'
    download_tag_2 = '//div[@class="ant-row ant-form-item"]//div[@class="ant-form-item-control"]//button'
    op.roll_down_window(download_tag_1)
    op.delete_file()
    #print("delete finish")

    selector_xpaths = []
    for i in range(1,4):
        selector_xpath = '//div[@class="ant-modal-root"]/../following-sibling::div[2]//ul[@class="ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical"]//li[{}]'.format(
            i)
        # selector_xpath = "//div[@style=\"width: 200px; left: 224px; top: 227px;\"]//ul[@class=\"ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical\"]//li[{}]".format(
        #     i)
        #selector_xpath = "//ul[@class=\"ant-select-dropdown-menu ant-select-dropdown-menu-vertical  ant-select-dropdown-menu-root\"]//li[{}]".format(i)
        selector_xpaths.append(selector_xpath)
    date_xpath = "//ul[@role=\"listbox\"]//li[2]"

    file_class = ['申购一(拉新)', '申购二(满减)', '定投']
    for index, selector_xpath in enumerate(selector_xpaths):
        op.click(download_tag_1)
        # 点击下载类型
        if index == 0:
            pass
        else:
            # time.sleep(1)
            op.click(
                '//label[@title="请选择下载类型"]/../following-sibling::div[1]//div[@class="ant-select-selection__rendered"]')
            # op.click(
            #     '//div[@class="ant-modal-content"]//div[@class="ant-form-item-control has-success"]//div[@class="ant-select-selection__rendered"]')
            # time.sleep(1)
            # driver.find_elements_by_xpath('//ul[@class="ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical"]')[0].find_elements_by_xpath('//li')[1].click()
            #
            op.click(selector_xpath)
        # time.sleep(1)
        op.click('//label[@title="选择明细报表"]/../following-sibling::div[1]//div[@class="ant-select-selection__rendered"]')
        # op.click(
        #    '//div[@class="ant-modal-content"]//div[@class="ant-form-item-control"]//div[@class="ant-select-selection__rendered"]')
        #op.click(selector_xpaths[1])
        # time.sleep(1)
        op.click(date_xpath)
        # time.sleep(1)
        op.click(download_tag_2)
        time.sleep(2)
        op.file_rename(file_class[index])
    driver.back()


if __name__ == '__main__':
    run_operation()
