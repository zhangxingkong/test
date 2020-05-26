from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from operation import Operation
import time
import random
import threading
from queue import Queue
import requests
import pandas as pd
import csv
import os

# 天天基金网络爬虫

LOG_COOKIES = []
BASE_URL = 'https://mycaifuhao.eastmoney.com/fund/report/PartialTradeTable?fcode='
headers = {
    'Referer': 'https://mycaifuhao.eastmoney.com/fund/report/tradedata',
}

funds_df = pd.DataFrame()
gLock = threading.Lock()
FILE_PATH = os.path.join(os.getcwd(), 'data/fund_info.csv')

class main(object):
    def __init__(self):
        # # 配置chrome下载对话框的参数
        # options = webdriver.ChromeOptions()
        # prefs = {'profile.default_content_settings.popups': 0, }
        # options.add_experimental_option('prefs', prefs)
        # # 设置开发者模式，防止被检测
        # options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # # 设置UA代理
        # # options.add_argument('user-agent=%s' % random.choice(proxies))
        # chrome_driver = r'E:\Anaconda\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
        # # options.add_argument('--headless')
        # # 初始化chrome浏览器
        # driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_driver)
        op = Operation()
        driver = op.driver
        driver.get('https://mycaifuhao.eastmoney.com/usercenter')
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, 'loginForm'))
        # )
        driver.maximize_window()
        time.sleep(5)
        op.switch_frame("//iframe[@name='my_iframe']")
        op.click("//input[@id='txt_account']")
        op.input_text('txt_account', '18317137759')
        op.click("//input[@id='txt_pwd']")
        op.input_text('txt_pwd', '999*htffund')
        time.sleep(1)
        op.click("//button[@id='btn_login']")
        time.sleep(1)
        op.click("//div[@class='em_init_icon']")
        global LOG_COOKIES
        LOG_COOKIES = driver.get_cookies()

        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            f.write('')
            f.close()

    def df_to_csv(self):
        pass


class Get_Json(threading.Thread):
    def __init__(self, ajax_queue, *args, **kwargs):
        super(Get_Json, self).__init__(*args, **kwargs)
        self.ajax_queue = ajax_queue
        self.session = requests.Session()
        for cookie in LOG_COOKIES:
            self.session.cookies.set(cookie['name'], cookie['value'])


    def run(self):
        global funds_df
        while self.ajax_queue.empty() is not True:
            fundcode = self.ajax_queue.get()
            url = '%s%s' % (BASE_URL, fundcode)
            response = self.session.get(url=url, headers=headers)
            fund_json = response.json()
            success_flag = fund_json['success']
            print(success_flag)
            print('='*30)
            fund_data = fund_json['data']
            fund_df = pd.DataFrame()
            if fund_data:
                fund_df = self.parse_data(fund_data)
                values = fund_df.loc('0').values
                gLock.acquire()
                # pd.concat([funds_df, fund_df], axis=0, ignore_index=True)
                # 第一种 CSV库写入方式
                with open(FILE_PATH, 'a', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(values)
                # 第二种 pandas库写入方式
                pd.to_csv(FILE_PATH, mode='a', header=False, index=False)
                gLock.release()
            else:
                pass




    def parse_data(self, fund_data):
        fund_df = pd.read_html(fund_data, encoding='utf-8')[0]
        fund_df.sort_values(by='日期', ascending=False)
        fund_df = fund_df.loc('0')
        print(fund_df)
        print('='*30)
        return fund_df




if __name__ == '__main__':
    main = main()
    ajax_queue = Queue(100)
    for fundcode in ['', '000696']:
        ajax_queue.put(fundcode)
    for i in range(2):
        t = Get_Json(ajax_queue)
        t.start()
