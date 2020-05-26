from selenium.common.exceptions import ElementNotVisibleException

from chaojiying import Chaojiying_Client
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image
import pandas as pd
# import zipfile
import zipfile_fix
import requests
import time
import os
import random
import datetime
import re
import json
import csv

# 登录 url
Login_Url = 'https://wshop.alipay.com/'

FILE_PATH = os.path.join(os.getcwd(), 'data')

USERNAME = '99fund@htffund.com'
#USERNAME = 'sun8029554'
PASSWD = "htf99!123"
#PASSWD = 'sun20021323'

# 跑数用参数，默认为1
days_elapse = 1

# 第二天上午跑程序用
# days_elapse = 2


# 操作类
class Operation(object):
    def __init__(self):
        # 对接已打开的浏览器
        chrome_options = webdriver.ChromeOptions()
        # prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': FILE_PATH, 'debuggerAddress':'127.0.0.1:9222'}
        # chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_experimental_option("debuggerAddress",
                                               "127.0.0.1:9222")
        # headers = {
        #     'Referer':"https://authstl.alipay.com/login/index.htm",
        #     'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        # }
        # chrome_options.add_argument('Referer="https://authstl.alipay.com/login/index.htm"')
        # chrome_options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"')
        chrome_driver = r'E:\\goodStudy\\spider\\chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_driver,
                                       chrome_options=chrome_options)

        # # 配置chrome下载对话框的参数
        # options = webdriver.ChromeOptions()
        # prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': FILE_PATH}
        # options.add_experimental_option('prefs', prefs)
        # # 设置开发者模式，防止被检测
        # options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # # 设置UA代理
        # # options.add_argument('user-agent=%s' % random.choice(proxies))
        # chrome_driver = r'E:\spider_app\chromedriver.exe'
        # # options.add_argument('--headless')
        # # 初始化chrome浏览器
        # self.driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_driver)

        # selenium headless 启动无头模式
        # options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')
        # profile = webdriver.FirefoxProfile()
        # self.driver = webdriver.Firefox(profile, executable_path=r'E:\spider_app\geckodriver', options=options)

    # 带有id属性的标签点击
    def click_id(self, xpath):
        self.driver.find_element_by_id(xpath).click()
        time.sleep(3)

    # 标签点击
    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(3)

    # 时间弹出框选择
    def click_time(self, xpath):
        local_time = time.localtime(time.time())
        click_time_1 = time.strftime('%Y{y}%m{m}%d{d}', time.localtime(time.mktime(local_time) - 6 * 24 * 60 * 60)) \
            .format(y='年', m='月', d='日')
        click_time_2 = time.strftime('%Y{y}%m{m}%d{d}',
                                     local_time).format(y='年', m='月', d='日')

        click_xpath_1 = xpath + '"' + click_time_1 + '"]'
        click_xpath_2 = xpath + '"' + click_time_2 + '"]'
        self.driver.find_element_by_xpath(click_xpath_1).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(click_xpath_2).click()
        time.sleep(2)

    # 下拉滚动条到指定元素位置
    def roll_down_window(self, xpath):
        target = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 上拉滚动条到最顶端
    def roll_up_window(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    # 文本输入
    def input_text(self, xpath, text):
        element = self.driver.find_element_by_id(xpath)
        element.clear()
        for i in text:
            element.send_keys(i)
            time.sleep(random.uniform(0, 0.5))

    # 截图
    def screen_shot(self, xpath):
        img_ele = self.driver.find_element_by_id(xpath)
        locations = img_ele.location
        sizes = img_ele.size
        rangle = (int(locations['x']), int(locations['y']),
                  int(locations['x'] + sizes['width']),
                  int(locations['y'] + sizes['height']))
        self.driver.save_screenshot('login.png')
        print(rangle)
        rangle = (1378, 516, 1498, 576)
        img1 = Image.open('login.png')
        img2 = img1.crop(rangle)
        img2.save('code.png')

    # 识别验证码
    def recognize_code(self):
        chaojiying = Chaojiying_Client('17709608161', 'a17709608161.',
                                       '897923')
        im = open('code.png', 'rb').read()
        code_data = chaojiying.PostPic(im, 1902)
        code = code_data['pic_str']
        return code

    # 登录
    def login(self, xpath1, xpath2, xpath3, xpath4, xpath5, xpath6, xpath7,
              account, pwd):
        """
        :param xpath1: 主页面登录xpath路径
        :param xpath2: 账密登录xpath路径
        :param xpath3: 账号输入xpath路径
        :param xpath4: 密码输入xpath路径
        :param xpath5: 验证码图片xpath路径
        :param xpath6: 验证码输入xpath路径
        :param xpath7: 点击登录xpath路径
        :param account: 账号
        :param pwd: 密码
        """
        self.driver.get(Login_Url)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        self.click(xpath1)  # 主页面登录跳转
        time.sleep(2)
        self.click(xpath2)  # 账密登录方式

        self.click_id(xpath3)
        self.input_text(xpath3, account)  # 账号
        self.click_id(xpath4)
        self.input_text(xpath4, pwd)  # 密码

        self.screen_shot(xpath5)  # 截图
        try:
            code = self.recognize_code()  # 识别验证码
            self.click_id(xpath6)
            self.input_text(xpath6, code)  # 验证码
            self.click_id(xpath7)
        except ElementNotVisibleException as e:
            print(e)

        while (True):
            time.sleep(5)
            self.click_id(xpath4)
            self.input_text(xpath4, pwd)  # 密码
            time.sleep(2)
            input()
            self.click_id(xpath7)

    # 切换frame
    def switch_frame(self, xpath):
        frame = self.driver.find_element_by_xpath(xpath)
        self.driver.switch_to.frame(frame)

    # 跳出当前frame
    def quit_frame(self):
        self.driver.switch_to.parent_frame()

    # 数据写入
    def data_write(self, item_cols, item_list, name):
        base_dir = os.getcwd()
        # item_cols = ('rank_type', 'rank', 'rank_content', 'time')
        file_name = os.path.join(base_dir, 'data', name)
        line = ''
        with open(file_name, 'ab') as f:
            for item in item_list:
                for col in item_cols:
                    try:
                        line = line + str(item[col]) + '^'
                    except:
                        line += '^'

                line = line[:-1] + '\n'
                f.write(line.encode('UTF-8'))
                line = ''

    # 删除截图
    def remove_pic(self):
        files = os.listdir('.')
        for file in files:
            if file.endswith('.png'):
                os.remove(file)

    # 解析xml文件
    def xml_to_csv(self, name):
        file_list = os.listdir('data')
        for file_name in file_list:
            if file_name.endswith('.xls'):
                with open('data/' + file_name, 'r', encoding='utf8') as f:
                    xml_data = f.read()

                soup = BeautifulSoup(xml_data, 'xml')
                # 获取到xml文件中第一个tagName为table的节点
                table = soup.find_all('Table')[0]

                lis = []
                for tr in table.findAll('Row'):
                    each_line = []
                    for td in tr.findAll('Cell'):
                        # print(td.getText())
                        each_line.append(td.getText().strip())
                    lis.append(each_line)
                result_df = pd.DataFrame(lis)
                # 第三行的所有列作为该dataFrame的列名
                columns = list(result_df.loc[2, :])
                result_df.columns = columns
                # 第四行到倒数第三行作为该dataFrame的数据
                result_df = result_df.iloc[3:-2]
                result_df['数据批次'] = time.strftime("%Y-%m-%d %H:00:00",
                                                  time.localtime())
                # save_path = os.path.join(os.getcwd(), 'data')
                result_df.to_csv('data/' + name, index=None, header=None)

                time.sleep(3)

                os.remove('data/' + file_name)

                time.sleep(1)

    # 文件重命名
    def file_rename(self, file_class):
        file_list = os.listdir('data')

        for file_name in file_list:
            if file_name.startswith('2'):
                os.rename('data/' + file_name,
                          'data/' + file_class + file_name)

    # 删除文件夹中指定文件
    def delete_file(self):
        file_list = os.listdir('data')

        for file_name in file_list:
            if '申购' in file_name or '定投' in file_name:
                os.remove('data/' + file_name)

    # 解压文件
    def unzip(self):
        file_list = os.listdir('data')

        for file_name in file_list:
            if file_name.endswith('.zip'):
                fz = zipfile_fix.ZipFile('data/' + file_name, 'r')
                fz.extractall('data')
                time.sleep(1)
                fz.close()

                os.remove('data/' + file_name)

                # # csv文件重命名
                # def csv_rename(self, name):
                #     file_list = os.listdir('data')
                #
                #     for file_name in file_list:
                #         if file_name.endswith('.csv'):
                #             os.rename('data/'+file_name, 'data/'+name+'.csv')

                # time.sleep(1)

                # def csv_prefix(self, name):
                #     file_list = os.listdir('data')
                #
                #     for file_name in file_list:
                #         if file_name.endswith('.csv'):
                #             # os.rename('data/' + file_name, 'data/' + name + '_'+ file_name[: -4])
                #             df = pd.read_csv('data/'+file_name, encoding='gbk')
                #             df.to_csv('data/'+name+'_'+file_name[: -4], encoding='gbk', index=False)
                #             os.remove('data/'+file_name)
                #
                #     f_list = os.listdir('data')
                #     for f in f_list:
                #         if f.startswith(name):
                #             os.rename('data/'+f, 'data/'+f+'.csv')

                # time.sleep(1)

    # 合并csv文件
    def merge_csv(self, name):
        file_list = os.listdir('data')
        # print('file_list:', file_list)
        csv_list = []
        for file in file_list:
            if file.startswith(name) and (file != 's_sp_alipay_trade'):
                csv_list.append(file)

        # print('csv_list:', csv_list)
        for csv in csv_list:
            # try:
            #     df = pd.read_csv(open('data/'+csv, encoding='utf8'), header=None, engine='python')
            #     df.to_csv('data/'+name, mode='a', index=False, header=False)
            # except Exception as e:
            #     print('merge_csv-err:', e)
            #     print('merge_csv-err-csv:', csv)
            try:
                f = open('data/' + csv, encoding='utf8')
                df = pd.read_csv(f, header=None, engine='python')
                f.close()
                # df = pd.read_csv('data/'+csv, header=None, engine='python')
            except Exception as e:
                f.close()
                df = pd.DataFrame()
                print('merge-csv-error:', e)
                print('merge-csv-error-file:', csv)

            df.to_csv('data/' + name, mode='a', index=False, header=False)

        for f in csv_list:
            try:
                time.sleep(1)
                os.remove('data/' + f)
            except IOError as e:
                # print('errer:', e)
                print('系统错误无法删除文件:', f, '等待后续删除！')
                # csv_list.append(f)
                time.sleep(random.uniform(1, 2))
                continue

    # 数据增量
    def increment(self):
        yesterday = time.strftime(
            '%Y-%m-%d',
            time.localtime(time.time() - 24 * 60 * 60 * days_elapse))
        two_days_ago = time.strftime(
            '%Y-%m-%d',
            time.localtime(time.time() - 24 * 60 * 60 * (days_elapse + 1)))
        file_list = os.listdir('data')

        for name in file_list:
            if name != 's_sp_alipay_campaign_configure' and name != 's_sp_alipay_user_component' and name != 's_sp_alipay_profile' and (
                    'history' not in name):
                with open('data/' + name, 'r', encoding='utf8') as f:
                    lines = f.readlines()
                print('increment-file:', name)
                os.remove('data/' + name)
                # with open('data/'+name + '_history', 'a', encoding='utf8') as f:
                with open('data/' + name, 'a', encoding='utf8') as f:
                    for line in lines:
                        # line[: 10] : 2019-08-26
                        if line[:
                                10] == yesterday and name != 's_sp_alipay_trade':
                            f.write(line)
                        if line[:
                                10] == two_days_ago and name == 's_sp_alipay_trade':
                            f.write(line)

    # 补数增量
    def data_add(self, start_time, end_time):
        '''
        :param start_time: 开始日期 格式 ：‘2019-07-22’
        :param end_time: 截至日期
        :return:
        '''
        date_list = self.get_between_day(start_time, end_time)

        start_time_onedayago = str(
            datetime.datetime.strptime(start_time, '%Y-%m-%d') -
            datetime.timedelta(days=1))[:10]
        end_time_onedayago = str(
            datetime.datetime.strptime(end_time, '%Y-%m-%d') -
            datetime.timedelta(days=1))[:10]
        trade_date_list = self.get_between_day(start_time_onedayago,
                                               end_time_onedayago)

        file_list = os.listdir('data')

        for name in file_list:
            if name != 's_sp_alipay_campaign_configure' and name != 's_sp_alipay_user_component' and name != 's_sp_alipay_profile' and (
                    'history' not in name):
                with open('data/' + name, 'r', encoding='utf8') as f:
                    lines = f.readlines()
                print('increment-file:', name)
                # os.remove('data/'+name)
                with open('data/' + name + '_history', 'a',
                          encoding='utf8') as f:
                    # with open('data/'+name , 'a', encoding='utf8') as f:
                    for line in lines:
                        if line[:
                                10] in date_list and name != 's_sp_alipay_trade':
                            f.write(line)
                        if line[:
                                10] in trade_date_list and name == 's_sp_alipay_trade':
                            f.write(line)

    def transfer(self):
        file_list = os.listdir('data')
        for name in file_list:
            if name.endswith('.csv'):
                with open('data/' + name, 'r', encoding='gbk') as f:
                    lines = f.readlines()
                    lines.remove(lines[0])
                    # print(lines)
                    lines = [line.replace('=', '') for line in lines]
                    lines = [line.replace('"', '') for line in lines]

                with open('data/s_sp_alipay_campaign', 'a',
                          encoding='gbk') as f:
                    for line_data in lines:
                        f.write(line_data)

                os.remove('data/' + name)

    def quit(self):
        self.driver.quit()

    # 获取首页排行榜、交易量json数据
    def rank_str_to_csv(self, html_str):
        pattern = re.compile(r'<pre.+?(?<=>)(.+?)(?=<)')
        result = re.search(pattern, html_str)
        # print(html_str)
        rank_json = result.group(1)
        tmp_dir = json.loads(rank_json, encoding='utf-8')
        # 生成排行榜csv
        rank_tmp_dir = tmp_dir['queryFundRankRes']['results']
        rank_list = []
        for fund in rank_tmp_dir:
            fundcode, amount = (fund['fundCode'], fund['amount']['value'])
            # fundcode = fund['fundCode']
            # amount = fund['amount']['value']
            rank_list.append((fundcode, amount))
        headers = ['fundcode', 'amount']
        with open('data/product_trade_rank.csv',
                  'w+',
                  encoding='utf-8',
                  newline='') as fp:
            writer = csv.writer(fp)
            # writer.writerow(headers)
            writer.writerows(rank_list)
            fp.close()
        # 生成交易量csv
        inst_tmp_dir = tmp_dir['queryInstRes']['results'][0]['amountDetail']
        inst_list = []
        time_stamp_list = sorted(list(inst_tmp_dir.keys()))
        # print(time_stamp_list)
        for time_stamp in time_stamp_list:
            local_time = time.strftime("%Y-%m-%d %H:%M:%S",
                                       time.localtime(int(time_stamp) / 1000))
            amount = inst_tmp_dir[time_stamp]['value']
            inst_list.append((local_time, amount))
        headers = ['time', 'amount']
        with open('data/product_trade_amount.csv',
                  'w+',
                  encoding='utf-8',
                  newline='') as fp:
            writer = csv.writer(fp)
            # writer.writerow(headers)
            writer.writerows(inst_list)
            fp.close()

    # 获取用户画像json数据
    def get_json_data(self):
        cookies = self.driver.get_cookies()

        req = requests.Session()
        for cookie in cookies:
            req.cookies.set(cookie['name'], cookie['value'])

        date = time.strftime(
            '%Y%m%d',
            time.localtime(time.time() - 24 * 60 * 60 * (days_elapse + 1)))
        json_url = 'https://wshop.alipay.com/api/dataAnalysis/index?date={}'.format(
            date)
        headers = {
            'Accept':
            'application/json',
            'Accept-Encoding':
            'gzip, deflate, br',
            'Accept-Language':
            'zh-CN,zh;q=0.9',
            'client-wshop-pid':
            '2088701481528372',
            'Connection':
            'keep-alive',
            'Content-Type':
            'application/json',
            'Host':
            'wshop.alipay.com',
            'Referer':
            'https://wshop.alipay.com/user_analysis',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }

        json_data = req.get(url=json_url, headers=headers).json()
        return json_data

    # 补充一段时间内的人物头像数据
    def get_json_data_list_add(self, start_time, end_time):
        cookies = self.driver.get_cookies()

        json_data_list = []

        date_list = self.get_between_day(start_time, end_time)

        req = requests.Session()
        for cookie in cookies:
            req.cookies.set(cookie['name'], cookie['value'])

        # date = time.strftime('%Y%m%d', time.localtime(time.time() - 24 * 60 * 60 * (days_elapse + 1)))

        headers = {
            'Accept':
            'application/json',
            'Accept-Encoding':
            'gzip, deflate, br',
            'Accept-Language':
            'zh-CN,zh;q=0.9',
            'client-wshop-pid':
            '2088701481528372',
            'Connection':
            'keep-alive',
            'Content-Type':
            'application/json',
            'Host':
            'wshop.alipay.com',
            'Referer':
            'https://wshop.alipay.com/user_analysis',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }

        for date in date_list:
            url_date = ''.join(date.split('-'))
            json_url = 'https://wshop.alipay.com/api/dataAnalysis/index?date={}'.format(
                date)
            json_data = req.get(url=json_url, headers=headers).json()
            json_data['date'] = date
            json_data_list.append(json_data)
        return json_data_list

    # 提取json数据
    def parse_json(self, dict_data):
        k_list = list(dict_data.keys())
        # print(k_list)
        crawl_time = time.strftime('%Y-%m-%d %H:00:00', time.localtime())
        date = time.strftime(
            '%Y-%m-%d',
            time.localtime(time.time() - 24 * 60 * 60 * (days_elapse + 1)))
        item_list = []
        user_item_list = []
        for i in k_list:
            if i == 'common' or i == 'identity':
                for k in list(dict_data[i].keys()):
                    for m in dict_data[i][k]:
                        item = {}
                        item['data_date'] = date
                        item['caption'] = k
                        item['classification'] = m['value']
                        item['classification_count'] = m['cnt']
                        item['user_type'] = 'A类用户'
                        item['crawl_time'] = crawl_time
                        # print(item)
                        item_list.append(item)
            elif i == 'yesterday':
                for j in dict_data[i]:

                    for n in j['distributed']:
                        user_item = {}
                        user_item['data_date'] = date
                        user_item['user_type'] = j['title']
                        user_item['crawl_time'] = crawl_time
                        user_item['total_count'] = j['cnt']
                        # component_item = {}
                        # component_item['component'] = n['title']
                        # component_item['count'] = n['from_cnt']
                        user_item['component'] = n['title']
                        user_item['component_count'] = n['from_cnt']
                        user_item['rate'] = '%.2f' % (
                            user_item['component_count'] /
                            user_item['total_count'])
                        user_item_list.append(user_item)

                        # for c_item in component_item_list:
                        #     user_item['component'] =

        total_counts = {}
        for item in item_list:
            try:
                total_counts[item['caption']] += item['classification_count']
            except:
                total_counts[item['caption']] = item['classification_count']

        # print(total_counts)

        for item in item_list:
            rate = item['classification_count'] / total_counts[item['caption']]
            data_rate = '%.2f' % rate
            item['rate'] = data_rate
            item['total_count'] = total_counts[item['caption']]
            # print(item)

        # for user_item in user_item_list:
        #     print(user_item)
        # print('item_list:', item_list)
        # print('user_item_list:', user_item_list)
        return item_list, user_item_list

    # 补充一段时间内的任务头像数据-提取json数据
    def parse_json_list_add(self, dict_data_list):
        item_list = []
        user_item_list = []
        n = 0
        for dict_data in dict_data_list:

            k_list = list(dict_data.keys())
            print('dict_data:', dict_data)
            print(k_list)
            crawl_time = time.strftime('%Y-%m-%d %H:00:00', time.localtime())
            # date = time.strftime('%Y-%m-%d', time.localtime(time.time() - 24 * 60 * 60 * (days_elapse + 1)))
            date = dict_data['date']
            for i in k_list:
                if i == 'common' or i == 'identity':
                    try:
                        for k in list(dict_data[i].keys()):
                            for m in dict_data[i][k]:
                                item = {}
                                item['data_date'] = date
                                item['caption'] = k
                                item['classification'] = m['value']
                                item['classification_count'] = m['cnt']
                                item['user_type'] = 'A类用户'
                                item['crawl_time'] = crawl_time
                                # print(item)
                                item_list.append(item)
                    except Exception as e:
                        print('user-error:', e)
                        print('error-data:', dict_data[i])
                        print('error-data:', date)

                elif i == 'yesterday':
                    for j in dict_data[i]:

                        for n in j['distributed']:
                            user_item = {}
                            user_item['data_date'] = date
                            user_item['user_type'] = j['title']
                            user_item['crawl_time'] = crawl_time
                            user_item['total_count'] = j['cnt']
                            # component_item = {}
                            # component_item['component'] = n['title']
                            # component_item['count'] = n['from_cnt']
                            user_item['component'] = n['title']
                            user_item['component_count'] = n['from_cnt']
                            user_item['rate'] = '%.2f' % (
                                user_item['component_count'] /
                                user_item['total_count'])
                            user_item_list.append(user_item)

                            # for c_item in component_item_list:
                            #     user_item['component'] =

            total_counts = {}
            for item in item_list:
                try:
                    total_counts[
                        item['caption']] += item['classification_count']
                except:
                    total_counts[
                        item['caption']] = item['classification_count']

            for item in item_list:
                rate = item['classification_count'] / total_counts[
                    item['caption']]
                data_rate = '%.2f' % rate
                item['rate'] = data_rate
                item['total_count'] = total_counts[item['caption']]

        return item_list, user_item_list

    # 给点时间段-获取时间列表
    def get_between_day(self, start_time, end_date=None):
        date_list = []
        start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d")
        if end_date is None:
            end_date = datetime.datetime.strptime(
                time.strftime('%Y-%m-%d', time.localtime(time.time())),
                "%Y-%m-%d")
        else:
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        while start_time <= end_date:
            date_str = start_time.strftime("%Y-%m-%d")
            date_list.append(date_str)
            start_time += datetime.timedelta(days=1)
        return date_list

    def change_windowhandler(self, website):
        self.driver.execute_script("window.open()")
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.get(website)


if __name__ == '__main__':
    op = Operation()
    # op.remove_pic()
    # print(os.listdir('.'))
    # op.unzip()
    # op.xml_to_csv('test')
    # op.merge_csv('test')
    # op.increment()
    # date_str = time.strftime('%Y-%m-%d', time.localtime(time.time() - 24 * 60 * 60))
    # with open('data/test', encoding='utf8') as f:
    #     lines_data = f.readlines()
    #     # print(data)
    #     # print(type(data))
    #     # print(data[: 10])
    #     # data2 = f.readline()
    #     # print(data2)
    # os.remove('data/test')
    # for line in lines_data:
    #     if line[: 10] == date_str:
    #         with open('data/test','a', encoding='utf8') as f:
    #             f.write(line)
    # with open('s_sp_campaign', 'r', encoding='gbk') as f:
    #     lines = f.readlines()
    #     lines.remove(lines[0])
    #     # print(lines)
    #     lines = [line.replace('=', '') for line in lines]
    #     lines = [line.replace('"', '') for line in lines]
    #
    # with open('s_sp_campaign_update', 'a', encoding='gbk') as f:
    #     for line_data in lines:
    #         f.write(line_data)
    # op.transfer()
    # op.merge_csv('s_sp_alipay_traffic')

    # 补数操作
    op.data_add('2019-09-18', '2019-09-21')
