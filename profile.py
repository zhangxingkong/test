import requests
import time
import json
from pprint import pprint
#from jsonpath import jsonpath
import time
from Conf import *
from operation import Operation


headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'client-wshop-pid': '2088701481528372',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Host': 'wshop.alipay.com',
    'Referer': 'https://wshop.alipay.com/user_analysis',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}


# response = requests.get(url, headers=headers)
#
# data = response.text
# print(type(data))
# print(data)


# rank_time = time.strftime('%Y%m%d', time.localtime(time.time()-24*60*60))
op = Operation()
driver = op.driver
url = 'https://wshop.alipay.com/'

USERNAME = '99fund@htffund.com'
PASSWD = 'htf99!123'

while True:
    try:
        driver.get(url)
        driver.implicitly_wait(3)
        driver.maximize_window()


        op.click(XPATH['homepage']['login_xpath'])
    except:
        time.sleep(2)
        # driver.quit()
    else:
        break

time.sleep(3)

op.click(XPATH['homepage']['login_way_xpath'])

op.click_id(ID_XPATH['login']['acc_xpath'])
op.input_text(ID_XPATH['login']['acc_xpath'], USERNAME)


op.click_id(ID_XPATH['login']['pwd_xpath'])
op.input_text(ID_XPATH['login']['pwd_xpath'], PASSWD)

try:
    op.screen_shot(ID_XPATH['login']['img_xpath'])
    code = op.recognize_code()
    op.click_id(ID_XPATH['login']['code_xpath'])
    op.input_text(ID_XPATH['login']['code_xpath'], code)
except:
    pass

op.remove_pic()
op.click_id(ID_XPATH['login']['login_bt_xpath'])

driver.find_element_by_xpath('//a[text()="用户画像"]').click()
time.sleep(5)

cookies = driver.get_cookies()
# print(cookies)

req = requests.Session()
for cookie in cookies:
    req.cookies.set(cookie['name'], cookie['value'])

for delta in range(1, 4):
    q_date = time.strftime('%Y%m%d', time.localtime(time.time() - 24 * 60 * 60 * delta))
    json_url = 'https://wshop.alipay.com/api/dataAnalysis/index?date={}'.format(q_date)
    dict_data = req.get(url=json_url, headers=headers).json()
    # print(type(json_data))
    # pprint(json_data)
    k_list = list(dict_data.keys())
    # print(k_list)
    crawl_time = time.strftime('%Y-%m-%d %H:00:00', time.localtime())
    date = time.strftime('%Y-%m-%d', time.localtime(time.time() - 24 * 60 * 60 * delta))
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
                    item['user_type'] = 'A类体验用户'
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
                    user_item['rate'] = '%.2f' % (user_item['component_count'] / user_item['total_count'])
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
    # return item_list, user_item_list
    file_date = time.strftime('%Y%m%d', time.localtime(time.time() - 24 * 60 * 60 * (delta-1)))
    profile_item_col = (
    'data_date', 'user_type', 'caption', 'classification', 'classification_count', 'total_count', 'rate', 'crawl_time')
    profile_export_file = 's_sp_alipay_profile.{}'.format(file_date)
    op.data_write(profile_item_col, item_list, profile_export_file)

    user_item_col = ('data_date', 'user_type', 'component', 'component_count', 'total_count', 'rate', 'crawl_time')
    user_export_file = 's_sp_alipay_user_component.{}'.format(file_date)
    op.data_write(user_item_col, user_item_list, user_export_file)
    time.sleep(3)
