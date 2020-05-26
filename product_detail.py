from operation import Operation
import re
import json
import time
import csv

def main():
    op = Operation()
    driver = op.driver
    driver.get('https://wshop.alipay.com/api/dashboard/queryProductData')
    html_str = driver.page_source
    pattern = re.compile(r'<pre.+?(?<=>)(.+?)(?=<)')
    result = re.search(pattern, html_str)
    result_json = result.group(1)
    result = json.loads(result_json)
    product_list = [] # 重点单品列表详情
    fundCode_list = [] # 重点单品基金号列表

    for product in result['productDetailList']:
        product_detail = []  # 单个重点单品交易时间序列
        fundCode = product['fundCode']
        fundCode_list.append(fundCode)
        fundName = product['fundName']
        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        redeemAmount = product['redeemAmount']
        tradeAmount = product['tradeAmount']
        tradeFundValue = product['tradeFundValue']
        product_list.append((fundCode, fundName, local_time, redeemAmount, tradeAmount, tradeFundValue))

        time_stamp_list = sorted(list(product['redeemAmountDetail'].keys()))
        for time_stamp in time_stamp_list:
            redeem_amount = product['redeemAmountDetail'][time_stamp]['value']
            trade_amount = product['tradeAmountDetail'][time_stamp]['value']
            local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time_stamp) / 1000))
            product_detail.append((local_time,redeem_amount,trade_amount))
        headers = ['time', 'redeem_amount', 'trade_amount']
        # 写入该单品交易详情时间序列
        filename = 'data/key_product_' + fundCode + '.csv'
        with open(filename, 'w', encoding='gbk', newline='') as fp:  # utf-8编码会有乱码
            writer = csv.writer(fp)
            # writer.writerow(headers)
            writer.writerows(product_detail)
            fp.close()

    # 写入重点单品列表
    headers = ['fundCode', 'fundName', 'time', 'redeemAmount', 'tradeAmount', 'value']
    with open('data/key_product_detail.csv', 'w', encoding='gbk', newline='') as fp:  # utf-8编码会有乱码
        writer = csv.writer(fp)
        # writer.writerow(headers)
        writer.writerows(product_list)
        fp.close()
    time.sleep(2)
    driver.back()
    time.sleep(3)

    # 写入各单品用户分布
    for fundCode in fundCode_list:
        user_url = 'https://wshop.alipay.com/api/dashboard/querySingleFundUserData?fundCode=' + fundCode
        driver.get(user_url)
        user_html_str = driver.page_source
        user_pattern = re.compile(r'<pre.+?(?<=>)(.+?)(?=<)')
        user_result = re.search(user_pattern, user_html_str)
        user_result_json = user_result.group(1)
        user_result = json.loads(user_result_json)
        user_data_list = []
        for item in user_result['userDetailRes']['results']:
            tradeType = item['tradeType']
            userType = item['userType']
            amount = item['amount']['value']
            user_data_list.append((fundCode,tradeType,userType,amount))
        headers = ['fundCode', 'tradeType', 'userType','amount']
        # 写入该单品用户分布csv
        filename = 'data/user_distribution_' + fundCode + '.csv'
        with open(filename, 'w', encoding='gbk', newline='') as fp:  # utf-8编码会有乱码
            writer = csv.writer(fp)
            # writer.writerow(headers)
            writer.writerows(user_data_list)
            fp.close()
        time.sleep(2)
        driver.back()
        time.sleep(3)






if __name__ == '__main__':
    main()