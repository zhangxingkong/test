import selenium

from operation import Operation
import re
import json
import time
import datetime
import csv


def main():
    op = Operation()
    driver = op.driver
    driver.get('https://wshop.alipay.com/op-overview?activeKey=target')
    time.sleep(3)
    driver.switch_to.frame('myreports-target')  # 必须
    date_xpath = "//span[text()='最新数据截止：']/following-sibling::span"
    date = driver.find_element_by_xpath(
        date_xpath).get_attribute('textContent')
    data_list = []

    # 获取第一行 index_list缺少第一个 原因未知 可优化 TODO
    one_line = [date]
    xpath = "//div[@class='ant-select-selection-selected-value']"
    one_line.append(driver.find_element_by_xpath(
        xpath).get_attribute('textContent'))
    try:
        xpath = "//p[text()='最新本机构排名']/following-sibling::div/p/span"
        rank_of_this_institution = driver.find_element_by_xpath(
            xpath).get_attribute('textContent')
    except selenium.common.exceptions.NoSuchElementException:
        rank_of_this_institution = '无'
    one_line.append(rank_of_this_institution)
    # 读取前十
    xpath = "//div[@class='ant-col-12']//span"
    rank_list = driver.find_elements_by_xpath(xpath)  # 当前指标前十列表
    for rank in rank_list:
        one_line.append(rank.get_attribute('textContent'))
    data_list.append(one_line)

    # 点击指标列表
    select_xpath = "//div[@class='ant-select-selection__rendered']"
    op.click(select_xpath)

    xpath = "//li[@class='ant-select-dropdown-menu-item']"
    index_list = driver.find_elements_by_xpath(xpath)  # 指标列表
    length = len(index_list)
    # 关闭指标列表
    select_xpath = "//div[@class='ant-select-selection__rendered']"
    op.click(select_xpath)

    for i in range(length):
        one_line = [date]
        # 再打开指标列表
        op.click(select_xpath)
        index = index_list[i].get_attribute('textContent')
        one_line.append(index)
        index_list[i].click()
        time.sleep(3)
        # 读取本机构排名
        try:
            xpath = "//p[text()='最新本机构排名']/following-sibling::div/p/span"
            rank_of_this_institution = driver.find_element_by_xpath(
                xpath).get_attribute('textContent')
        except selenium.common.exceptions.NoSuchElementException:
            rank_of_this_institution = '无'
        one_line.append(rank_of_this_institution)
        # 读取前十
        xpath = "//div[@class='ant-col-12']//span"
        rank_list = driver.find_elements_by_xpath(xpath)  # 当前指标前十列表 2-10
        for rank in rank_list:
            one_line.append(rank.get_attribute('textContent'))
        data_list.append(one_line)

    headers = ['date', 'index', 'rank']
    for i in range(1, 11):
        headers.append('rank_{}'.format(i))

    with open('data/institution_rank.csv', 'w', encoding='gbk', newline='') as fp:  # utf-8编码会有乱码
        writer = csv.writer(fp)
        # writer.writerow(headers)
        writer.writerows(data_list)
        fp.close()
    time.sleep(2)
    driver.get('https://wshop.alipay.com/home')
    time.sleep(3)

    # xpath = "//p[text()='最新本机构排名']/following-sibling::div/p/span"
    # text = driver.find_element_by_xpath(xpath).get_attribute('textContent')
    # print(text)


if __name__ == '__main__':
    main()
