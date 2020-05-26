from operation import Operation
import re
import json
import time
import datetime
import csv

def main():
    date = (datetime.datetime.now() - datetime.timedelta(days=2))
    date = date.strftime("%Y-%m-%d")
    op = Operation()
    driver = op.driver
    driver.get('https://wshop.alipay.com/api/queryForumInteractData?endTime='+date) #日期限定，默认为前2天？
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
        interactUv1d = forum['interactUv1d']
        interactUv7d = forum['interactUv7d']
        interactUv30d = forum['interactUv30d']
        comValidReplyCnt1d = forum['comValidReplyCnt1d']
        comValidReplyCnt7d = forum['comValidReplyCnt7d']
        comValidReplyCnt30d = forum['comValidReplyCnt30d']
        comValidReplyUser1d = forum['comValidReplyUser1d']
        comValidReplyUser7d = forum['comValidReplyUser7d']
        comValidReplyUser30d = forum['comValidReplyUser30d']
        comValidPopCnt1d = forum['comValidPopCnt1d']
        comValidPopCnt7d = forum['comValidPopCnt7d']
        comValidPopCnt30d = forum['comValidPopCnt30d']
        comValidFavorCnt1d = forum['comValidFavorCnt1d']
        comValidFavorCnt7d = forum['comValidFavorCnt7d']
        comValidFavorCnt30d = forum['comValidFavorCnt30d']
        data_list.append((forumNameAbbr,rptDate,companyNameAbbr,forumId,fundCode,forumTypeName,
                          interactUv1d,interactUv7d,interactUv30d,comValidReplyCnt1d,comValidReplyCnt7d,
                          comValidReplyCnt30d,comValidReplyUser1d,comValidReplyUser7d,comValidReplyUser30d,
                          comValidPopCnt1d,comValidPopCnt7d,comValidPopCnt7d,comValidPopCnt30d,
                          comValidPopCnt30d,comValidFavorCnt1d,comValidFavorCnt7d,comValidFavorCnt30d))
    headers = ['forumNameAbbr','rptDate','companyNameAbbr','forumId','fundCode','forumTypeName',
                'interactUv1d','interactUv7d','interactUv30d','comValidReplyCnt1d','comValidReplyCnt7d',
                'comValidReplyCnt30d','comValidReplyUser1d','comValidReplyUser7d','comValidReplyUser30d',
                'comValidPopCnt1d','comValidPopCnt7d','comValidPopCnt7d','comValidPopCnt30d',
                'comValidPopCnt30d','comValidFavorCnt1d','comValidFavorCnt7d','comValidFavorCnt30d']
    with open('data/interact_analyze.csv', 'w', encoding='gbk', newline='') as fp:  # utf-8编码会有乱码
        writer = csv.writer(fp)
        # writer.writerow(headers)
        writer.writerows(data_list)
        fp.close()
    time.sleep(2)
    driver.back()
    time.sleep(3)


if __name__ == '__main__':
    main()