from operation import Operation
import re
import json
import csv

def main():
    op = Operation()
    driver = op.driver
    num = 1000 #读取多少条数据，目前一共仅50多条

    driver.get('https://wshop.alipay.com/api/investmentFreeRide/index?pageIndex=1&pageSize={}'.format(num))
    html_str = driver.page_source

    pattern = re.compile(r'<pre.+?(?<=>)(.+?)(?=<)')
    result = re.search(pattern, html_str)
    result_json = result.group(1)
    result = json.loads(result_json)
    investmentList = []
    for investment in result['InvestmentFreeRideList']:
        # print(investment)
        hotspotSubmitName, opinionId, workId, chanceIntro, \
        gmtCreate, operateTime, lastModifiedTime, workStatus = (investment['detail']['hotspotSubmitName'], #部分数据在detail二级目录下
                                                                investment['opinionId'],
                                                                investment['workId'],
                                                                investment['detail']['chanceIntro'],
                                                                investment['gmtCreate'],
                                                                investment['operateTime'],
                                                                investment['lastModifiedTime'],
                                                                investment['workStatus'])
        investmentList.append((hotspotSubmitName, opinionId, workId, chanceIntro, \
        gmtCreate, operateTime, lastModifiedTime, workStatus))

    headers = ['热点名称', '解读ID','流水','机会简述','创建时间','更新时间','解读更新时间','状态']

    with open('data/investment_chance.csv', 'w', encoding='gbk', newline='') as fp:  #utf-8编码会有乱码
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(investmentList)
        fp.close()

if __name__ == '__main__':
    main()