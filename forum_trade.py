from operation import Operation
import re
import json
import time
import datetime
import csv

def main():
    # date = (datetime.datetime.now() - datetime.timedelta(days=1))
    # date = date.strftime("%Y-%m-%d")
    op = Operation()
    driver = op.driver
    driver.get('https://wshop.alipay.com/api/queryForumTradeData') #暂时不加日期限定，默认为前一天？
    html_str = driver.page_source
    pattern = re.compile(r'<pre.+?(?<=>)(.+?)(?=<)')
    result = re.search(pattern, html_str)
    result_json = result.group(1)
    result = json.loads(result_json)
    data_list = []
    for forum in result['forumMesaDatas']:
        forumNameAbbr = forum['forumNameAbbr']
        rptDate = forum['rptDate']
        companyNameAbbr = forum['companyNameAbbr']
        forumId = forum['forumId']
        fundCode = forum['fundCode']
        forumTypeName = forum['forumTypeName']
        fundPayUv1d = forum['fundPayUv1d']
        fundPayCnt1d = forum['fundPayCnt1d']
        fundPayAmount1d = forum['fundPayAmount1d']
        fundPayKedan1d = forum['fundPayKedan1d'] # 成交客单价
        fundActivePayUv1d = forum['fundActivePayUv1d']
        fundActivePayCnt1d = forum['fundActivePayCnt1d']
        fundActivePayAmount1d = forum['fundActivePayAmount1d']
        fundActivePayKedan1d = forum['fundActivePayKedan1d'] # 主动成交客单价
        fundFixedUv1d = forum['fundFixedUv1d']
        fundFixedAmount1d = forum['fundFixedAmount1d']
        data_list.append((forumNameAbbr,rptDate,companyNameAbbr,forumId,fundCode,forumTypeName,
                          fundPayUv1d,fundPayCnt1d,fundPayAmount1d,fundPayKedan1d,fundActivePayUv1d,
                          fundActivePayCnt1d,fundActivePayAmount1d,fundActivePayKedan1d,fundFixedUv1d,
                          fundFixedAmount1d))
    headers = ['forumNameAbbr','rptDate','companyNameAbbr','forumId','fundCode','forumTypeName',
                'fundPayUv1d','fundPayCnt1d','fundPayAmount1d','fundPayKedan1d','fundActivePayUv1d',
                'fundActivePayCnt1d','fundActivePayAmount1d','fundActivePayKedan1d','fundFixedUv1d',
                'fundFixedAmount1d']
    with open('data/forum_trade_analyze.csv', 'w', encoding='gbk', newline='') as fp:  # utf-8编码会有乱码
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(data_list)
        fp.close()
    time.sleep(2)
    driver.back()
    time.sleep(3)


if __name__ == '__main__':
    main()