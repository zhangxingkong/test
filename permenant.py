from operation import Operation
import time
import datetime
import rank_list
import product_detail
import platform_investment
import forum_visit_data
import interact_analyze
import forum_trade
import user_persona
import institution_rank
import os, shutil


def main():
    op = Operation()
    driver = op.driver
    rank_listCount = 0
    monthNow = 0
    dayNow = 0
    while (True):
        '''
        Several scripts to run
        '''
        # 基金交易额排行  产品交易量  重点详情单品
        if rank_listCount % 3 == 0:
            rank_list.main()  # 基金交易额排行  产品交易量
            product_detail.main()  # TODO 重点详情单品及详细信息、用户分布 多个产品是否需要并到一张表里？是否需要记录历史数据？
        rank_listCount += 1
        # 平台招商 拉新 满减 定投 每月一号运行一次或首次运行 需要去掉表头 TODO
        t = time.localtime()
        if (t.tm_mon != monthNow and t.tm_mday == 1) or monthNow == 0:
            monthNow = t.tm_mon
            # platform_investment.run_operation()

        # 每天10点运行一次
        if (t.tm_mday != dayNow and t.tm_hour == 10) or dayNow == 0:
            dayNow = t.tm_mday
            # 阵地流量讨论区数据 ？可以一次爬取多日数据 TODO
            forum_visit_data.main()
            # 互动内容分析 日期默认
            interact_analyze.main()
            # 讨论区交易分析 日期默认 可以添加 startTime endTime
            forum_trade.main()
            # 阵地流量用户画像 日期默认前两天 可修改
            user_persona.main()
            # 运营总览排名指标
            institution_rank.main()
            # 运营司南 交易分析 整体、个体 指标设置？ TODO

        # 新版阵地流量 TODO

        driver.refresh()  # or driver.get('https://wshop.alipay.com')
        # driver.get('https://wshop.alipay.com')
        movefiles('E:\\ftp\\ali_download')
        print(t)
        time.sleep(300)


def movefiles(dst):
    date = (datetime.datetime.now())
    date = date.strftime("%Y%m%d%H%M")
    srcPath = os.getcwd() + '\\data'
    fileList = os.listdir(srcPath)
    if os.path.exists(dst):
        for filename in fileList:
            dstPath = dst + '\\' + filename.split('.')[0] + '.' + date
            shutil.move(srcPath + '\\' + filename, dstPath)
    else:
        print('destination error')


if __name__ == '__main__':
    main()
