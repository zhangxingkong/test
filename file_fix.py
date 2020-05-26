import time
import requests
from Conf import *
from operation import Operation


# rank_time = time.strftime('%Y%m%d', time.localtime(time.time()-24*60*60))
op = Operation()
driver = op.driver
url = 'https://wshop.alipay.com/'

USERNAME = '99fund@htffund.com'
PASSWD = 'htfzfb!123'

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

op.click(XPATH['main_menu']['营销活动'])
trs = driver.find_elements_by_xpath('//tbody/tr')

n = 1
item_list = []
while n:
    for i in range(1, 6):
        # xpath = XPATH['marketing_activity']['campaign_status']
        # xpath = xpath[: -6] + '[{}]'.format(i) + xpath[-6:]
        # if driver.find_element_by_xpath(xpath).text != '已发布':
        #     n = 0
        #     break
        xp = XPATH['marketing_activity']['check']
        xp = xp[: 10] + '[{}]'.format(i) + xp[10:]
        try:
            op.click(xp)
        except:
            break

        time.sleep(2)

        div_list = driver.find_elements_by_xpath('//div[@class="ant-row campaign-info-item"]')
        item = {}
        for div in div_list[: -1]:

            k = div.find_element_by_xpath('./div[@class="ant-col-4 item-label"]').text
            if k == '红包核销情况':
                ths = div.find_elements_by_xpath('./div[@class="ant-col-20 item-value"]//th')
                tds = div.find_elements_by_xpath('./div[@class="ant-col-20 item-value"]//td')
                for m in range(0, 4):
                    k = ths[m].find_element_by_xpath('./span').text
                    v = tds[m].text
                    item[k] = v

            elif k == '奖品数量' or k == '已发放张数' or k == '剩余可发放奖品数' or k == '已恢复张数' or k == '已核销张数':
                v = div.find_element_by_xpath('./div[@class="ant-col-20 item-value"]').text[: -1]
                item[k] = int(v)

            else:
                try:
                    v = div.find_element_by_xpath('./div[@class="ant-col-20 item-value"]').text
                except:
                    try:
                        v = div.find_element_by_xpath('./div[@class="ant-col-20 sync-success item-value"]').text
                    except:
                        v = div.find_element_by_xpath('./div[@class="ant-col-20 sync-error item-value"]').text

                item[k] = v

        crawl_time = time.strftime('%Y-%m-%d %H:00:00', time.localtime())
        item['数据批次'] = crawl_time

            # time.sleep(5)
        item_list.append(item)

        driver.back()
        time.sleep(3)

    if driver.find_element_by_xpath(XPATH['marketing_activity']['next_page']).get_attribute('aria-disabled') == 'false':
        op.click(XPATH['marketing_activity']['next_page'])
    else:
        break

item_cols = (
    '活动触发类型',
    '活动目标',
    '活动名称',
    '活动状态',
    '活动操作状态',
    '活动开始时间',
    '活动结束时间',
    '活动生效时间段',
    '奖品数量',
    '每人累计领取上限',
    '是否自主发奖',
    '温馨提示',
    '温馨提示正文',
    '人群分组',
    '主推产品',
    '适用产品交易方式',
    '定投周期',
    '已发放张数',
    '剩余可发放奖品数',
    '已恢复张数',
    '已核销张数',
    '活动编号',
    '礼包券模板ID',
    '红包模板Id',
    '红包发放个数',
    '红包核销个数',
    '核销率',
    '数据批次'
)
op.data_write(item_cols, item_list, EXPORT_FILE['configure_export_file'])
