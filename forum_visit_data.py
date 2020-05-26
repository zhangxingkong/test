from operation import Operation
import re
import json
import time
import datetime
import csv

def main():
    #date = time.strftime("%Y-%m-%d", time.localtime())
    date = (datetime.datetime.now() - datetime.timedelta(days=2))
    date = date.strftime("%Y-%m-%d")
    op = Operation()
    driver = op.driver
    url = 'https://wshop.alipay.com/api/queryForumVisitData?endTime='+date+'&startTime='+date
    driver.get(url)
    html_str = driver.page_source
    pattern = re.compile(r'<pre.+?(?<=>)(.+?)(?=<)')
    result = re.search(pattern, html_str)
    result_json = result.group(1)
    result = json.loads(result_json)
    data_list = []
    for forum in result['forumMesaDatas']:
        forumNameAbbr = forum['forumNameAbbr']
        companyNameAbbr = forum['companyNameAbbr']
        forumId = forum['forumId']
        fundCode = forum['fundCode']
        forumTypeName = forum['forumTypeName']
        pageVisitUv1d = forum['pageVisitUv1d']
        pageVisitUv7d = forum['pageVisitUv7d']
        pageVisitUv30d = forum['pageVisitUv30d']
        pagePeruserStaytime1d = forum['pagePeruserStaytime1d']
        pageVisitPerdays7d = forum['pageVisitPerdays7d']
        pageVisitPerdays30d = forum['pageVisitPerdays30d']
        retentionVisit1d = forum['retentionVisit1d']
        retentionVisit7d = forum['retentionVisit7d']
        retentionVisit30d = forum['retentionVisit30d']
        commentPeruserExpoCnt = forum['commentPeruserExpoCnt'] #人均曝光内容
        interactUv1d = forum['interactUv1d']
        contentProductCnt1d = forum['contentProductCnt1d']
        data_list.append((forumNameAbbr,date,companyNameAbbr,forumId,fundCode,forumTypeName,
                         pageVisitUv1d,pageVisitUv7d,pageVisitUv30d,pagePeruserStaytime1d,
                         pageVisitPerdays7d,pageVisitPerdays30d,retentionVisit1d,retentionVisit7d,
                         retentionVisit30d,commentPeruserExpoCnt,interactUv1d,contentProductCnt1d))
    headers = ['forumNameAbbr','date','companyNameAbbr','forumId','fundCode','forumTypeName',
                         'pageVisitUv1d','pageVisitUv7d','pageVisitUv30d','pagePeruserStaytime1d',
                         'pageVisitPerdays7d','pageVisitPerdays30d','retentionVisit1d','retentionVisit7d',
                         'retentionVisit30d','commentPeruserExpoCnt','interactUv1d','contentProductCnt1d']
    with open('data/forum_data.csv', 'w', encoding='gbk', newline='') as fp:  # utf-8编码会有乱码
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(data_list)
        fp.close()
    time.sleep(2)
    driver.back()
    time.sleep(3)


if __name__ == '__main__':
    main()