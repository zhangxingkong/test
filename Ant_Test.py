from selenium import webdriver
import time
from pprint import pprint
#from PIL import Image
from chaojiying import Chaojiying_Client
import os


def write_data(item, name):
    base_dir = os.getcwd()
    item_cols = ('rank', 'rank_content')

    file_name = os.path.join(base_dir, 'data', name)
    line = ''
    with open(file_name, 'ab') as f:
        for col in item_cols:
            try:
                line = line + str(item[col]) + ','
            except:
                line += ','

        line = line[:-1] + '\n'
        f.write(line.encode('UTF-8'))


# 配置chrome下载对话框的参数
options = webdriver.ChromeOptions()
FILE_PATH = os.path.join(os.getcwd(), 'data')
prefs = {
    'profile.default_content_settings.popups': 0,
    'download.default_directory': FILE_PATH
}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)
url = 'https://wshop.alipay.com/signin'
n = 1
input()
while n:
    try:
        driver.get(url)
        driver.implicitly_wait(3)
        driver.maximize_window()
        # input()
        # driver.find_element_by_xpath('//a[@class="btn-login"]').click()
    except:
        time.sleep(2)
        # driver.quit()
    else:
        n = 0
input()
time.sleep(3)
driver.find_element_by_xpath('//li[text()="账密登录"]').click()

USERNAME = '99fund@htffund.com'
PASSWD = 'htf99!123'

driver.find_element_by_id('J-input-user').click()
for i in USERNAME:
    driver.find_element_by_id('J-input-user').send_keys(i)
    time.sleep(0.5)
input()
driver.find_element_by_id('password_rsainput').click()
for k in PASSWD:
    driver.find_element_by_id('password_rsainput').send_keys(k)
    time.sleep(0.5)

# img_ele = driver.find_element_by_id('J-checkcode-img')
#
# if img_ele:
#
#     locations = img_ele.location
#     sizes = img_ele.size
#     rangle = (int(locations['x']), int(locations['y']), int(locations['x'] + sizes['width']), int(locations['y'] + sizes['height']))
#     driver.save_screenshot('login.png')
#     img1 = Image.open('login.png')
#     img2 = img1.crop(rangle)
#     img2.save('code.png')
#
#     chaojiying = Chaojiying_Client('17709608161', 'a17709608161.', '897923')
#     im = open('code.png', 'rb').read()
#     code_data = chaojiying.PostPic(im, 1902)
#     code = code_data['pic_str']
#     print(code)
#
#     driver.find_element_by_id('J-input-checkcode').click()
#     for j in code:
#         driver.find_element_by_id('J-input-checkcode').send_keys(j)
#         time.sleep(0.5)

time.sleep(20)

driver.find_element_by_id('J-login-btn').click()
time.sleep(3)

driver.find_element_by_xpath('//a[text()="运营总览"]').click()
time.sleep(3)
driver.find_element_by_xpath('//div[text()="排名指标"]').click()
time.sleep(15)

iframe_ele = driver.find_element_by_xpath('//div//iframe')

driver.switch_to.frame(iframe_ele)
time.sleep(5)

# drop_down = driver.find_element_by_xpath('//span[@class="ant-select-arrow"]')

# for m in range(1, 21):
#     item = {}
#     drop_down.click()
#     li_xpath = '//ul/li[{}]'.format(m)
#     try:
#         li_ele = driver.find_element_by_xpath(li_xpath)
#     except:
#         drop_down.click()
#         break
#     li_text = li_ele.text
#     print(li_text)
#     li_ele.click()
# rank_contents = driver.find_elements_by_xpath('//div[@class="ant-col-12"]/span')
# rank_time = time.strftime('%Y%m%d', time.localtime(time.time()-24*60*60))
# i = 1
# name = driver.find_element_by_xpath('//div[@class="ant-select-selection-selected-value"]').text
# name = name + '_' + rank_time
# rank_contents_list = []
# for content in rank_contents:
#     item = {}
#     item['rank'] = i
#     rank_content = content.text
#     item['rank_content'] = rank_content
#     rank_contents_list.append(rank_content)
#
#     write_data(item, name)
#
#     i += 1
#
# try:
#     htf_rank = driver.find_element_by_xpath('//p[@class="ft-16"]/span').text
#     if '汇添富' not in rank_contents_list:
#         htf_rank_item = {}
#         htf_rank_item['rank'] = htf_rank
#         htf_rank_item['rank_content'] = '汇添富'
#
#         write_data(htf_rank_item, name)
# except:
#     pass
driver.switch_to.parent_frame()

driver.find_element_by_xpath('//a[text()="营销活动"]').click()
