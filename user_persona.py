from operation import Operation
import re
import json
import time
import datetime
import csv

def main():
    date = (datetime.datetime.now() - datetime.timedelta(days=2))
    dateForUrl = date.strftime("%Y%m%d")
    date = date.strftime("%Y-%m-%d")
    op = Operation()
    driver = op.driver
    url ='https://wshop.alipay.com/api/dauUserAnalysis?date=' + dateForUrl + '&version=all'
    driver.get(url)
    html_str = driver.page_source
    pattern = re.compile(r'<pre.+?(?<=>)(.+?)(?=<)')
    result = re.search(pattern, html_str)
    result_json = result.group(1)
    result = json.loads(result_json)
    data_list = []
    headers = []
    data_list.append(date)
    headers.append('date')
    # 翻译字典
    translate_dict = {
        '在全平台当前是否签署定投协议':'fixed_investment_assigned_in_whole_platform_or_not',
        '是':'yes',
        '否': 'no',
        '性别':'sex',
        '男': 'male',
        '女': 'female',
        '用户风险等级':'user_risk_level',
        '用户风险等级1':'user_risk_level_1',
        '用户风险等级2': 'user_risk_level_2',
        '用户风险等级3': 'user_risk_level_3',
        '用户风险等级4': 'user_risk_level_4',
        '用户风险等级5': 'user_risk_level_5',
        '用户理财能力':'financial_management_ability',
        '多于10万，少于30万':'10w_to_30w',
        '多于1万，少于5万':'1w_to_5w',
        '多于30万，少于100万':'30w_to_100w',
        '多于5万，少于10万':'5w_to_10w',
        '少于1万':'0_to_1w',
        '在全平台持仓基金数':'num_of_funds_held_in_whole_platform',
        '0只':'0',
        '1只':'1',
        '2只':'2',
        '3只':'3',
        '4只':'4',
        '5只及以上': 'equal_or_greater_than_5',
        '在全平台持仓金额':'amount_held_in_whole_platform',
        '2000～5000元之间':'2000_to_5000',
        '5000元及以上':'equal_or_greater_than_5000',
        '600元以内':'less_than_600',
        '600～2000元之间':'600_to_2000',
        '在全平台交易基金数':'num_of_funds_traded_in_whole_platform',
        '在全平台是否购买货币基金':'money_fund_bought_in_whole_platform_or_not',
        '在本机构持仓基金数':'num_of_funds_held_in_this_institution',
        '在本机构是否持有FOF':'FOF_held_in_this_institution_or_not',
        '在本机构是否持有短期理财':'short_term_financial_management_held_in_this_institution_or_not',
        '用户理财认知':'user_financial_awareness',
        '中':'medium',
        '低':'low',
        '高':'high',
        '在全平台一个月内访问天数':'access_days_in_whole_platform_1month',
        '在全平台三个月内访问天数':'access_days_in_whole_platform_3month',
        '0次': '0_time',
        '10次以上':'greater_than_10_time',
        '1次':'1_time',
        '2~3次':'2_to_3_time',
        '4~5次':'4_to_5_time',
        '6~10次':'6_to_10_time',
        '在全平台交易笔数':'num_of_transactions_in_whole_platform',
        '0笔':'0_transaction',
        '1笔':'1_transaction',
        '2笔':'2_transaction',
        '3笔':'3_transaction',
        '4笔':'4_transaction',
        '5笔':'5_transaction',
        '6笔及以上': 'equal_or_greater_than_6_transaction',
        '在全平台是否持有货币型基金':'money_fund_held_in_whole_platform_or_not',
        '在全平台是否购买FOF基金':'FOF_bought_in_whole_platform_or_not',
        '在本机构是否持有QDII':'QDII_held_in_this_institution_or_not',
        '用户年龄':'user_age',
        '18 <= age < 25':'18_to_25_age',
        '18 &lt;= age &lt; 25':'18_to_25_age',
        '25 <= age < 30':'25_to_30_age',
        '25 &lt;= age &lt; 30':'25_to_30_age',
        '30 <= age < 35':'30_to_35_age',
        '30 &lt;= age &lt; 35':'30_to_35_age',
        '35 <= age < 40':'35_to_40_age',
        '35 &lt;= age &lt; 40':'35_to_40_age',
        '40 <= age < 45':'40_to_45_age',
        '40 &lt;= age &lt; 45':'40_to_45_age',
        '45 <= age < 50':'45_to_50_age',
        '45 &lt;= age &lt; 50':'45_to_50_age',
        'age >= 50':'equal_or_greater_than_50_age',
        'age &gt;= 50':'equal_or_greater_than_50_age',
        '使用本机构权益金额总数':'amount_of_equity_used_in_this_institution',
        '0~5元':'0_to_5_yuan',
        '5~10元':'5_to_10_yuan',
        '10~20元':'10_to_20_yuan',
        '20~50元':'20_to_50_yuan',
        '50元及以上':'equal_or_greater_than_50_yuan',
        '在全平台交易总金额':'total_amount_traded_in_whole_platform',
        '在全平台是否持有QDII':'QDII_held_in_whole_platform_or_not',
        '在本机构是否持有指数型基金':'index_fund_held_in_this_institution_or_not',
        '在本机构是否购买FOF':'FOF_bought_in_this_institution_or_not',
        '在本机构是否购买股票型基金':'stock_fund_bought_in_this_institution_or_not',
        '在本机构是否购买货币基金':'money_fund_bought_in_this_institution_or_not',
        '在全平台交易基金类型数':'num_of_fund_types_traded_in_whole_platform',
        '0类':'0_kind',
        '1类':'1_kind',
        '2类':'2_kind',
        '3类':'3_kind',
        '4类':'4_kind',
        '5类':'5_kind',
        '6类':'6_kind',
        '7类':'7_kind',
        '8类':'8_kind', # 可能有大于9的 TODO
        '9类':'9_kind',
        '在全平台是否持有指数型基金':'index_fund_held_in_whole_platform_or_not',
        '在全平台是否持有混合型基金':'hybrid_fund_held_in_whole_platform_or_not',
        '在全平台是否购买债券型基金':'bond_fund_bought_in_whole_platform_or_not',
        '在全平台是否购买混合型基金':'hybrid_fund_bought_in_whole_platform_or_not',
        '在全平台是否购买短期理财':'short_term_financial_management_bought_in_whole_platform_or_not',
        '在本机构持仓金额':'amount_held_in_this_institution',
        '在本机构是否购买QDII':'QDII_bought_in_this_institution_or_not',
        '在全平台是否持有股票型基金':'stock_fund_held_in_whole_platform_or_not',
        '在全平台是否购买QDII':'QDII_bought_in_whole_platform_or_not',
        '在全平台是否购买股票型基金':'stock_fund_bought_in_whole_platform_or_not',
        '在本机构持仓基金类型数':'num_of_fund_types_held_in_this_institution',
        '在本机构是否购买指数型基金':'index_fund_bought_in_this_institution_or_not',
        '在本机构是否购买混合型基金':'hybrid_fund_bought_in_this_institution_or_not',
        '在本机构是否购买短期理财':'short_term_financial_management_bought_in_this_institution_or_not',
        '在全平台是否购买指数型基金':'index_fund_bought_in_whole_platform_or_not',
        '在本机构收益率分布':'return_rate_in_this_institution',
        '5％以下':'less_than_005',
        '5%~10%之间':'005_to_010',
        '10%~20%之间':'010_to_020',
        '20%~50%之间':'020_to_050',
        '50%以上':'greater_than_050',
        '在本机构是否持有货币基金':'money_fund_held_in_this_institution_or_not',
        '在本机构累计交易基金数':'num_of_funds_traded_in_this_institution',
        '在本机构累计交易基金类型数':'num_of_fund_types_traded_in_this_institution',
        '用户城市等级':'user_city_level',
        '1线城市':'first_tier_city',
        '2线城市':'second_tier_city',
        '3线城市':'third_tier_city',
        '4线城市':'forth_tier_city',
        '5线城市':'fifth_tier_city', # 还有更多？ TODO
        '使用全平台权益金额总数':'amount_of_equity_used_in_whole_platform',
        '在本机构是否定投过基金':'ever_fixed_investment_in_this_institution_or_not',
        '在本机构相关页面三个月内访问天数':'access_days_in_this_institution_3month',
        '在本机构累计交易金额':'total_amount_traded_in_this_institution',
        '在全平台收益率分布':'return_rate_in_whole_platform',
        '在本机构是否签署定投协议':'fixed_investment_assigned_in_this_institution_or_not',
        '在本机构相关页面一个月内访问天数':'access_days_in_this_institution_1month',
        '是否关注本机构财富号':'follow_caifuhao_of_this_institution_or_not',
        '在全平台持仓基金类型数':'num_of_fund_types_held_in_whole_platform',
        '在全平台是否定投过基金':'ever_fixed_investment_in_whole_platform_or_not',
        '在全平台是否持有债券型基金':'bond_fund_held_in_whole_platform_or_not',
        '在全平台是否持有短期理财':'short_term_financial_management_held_in_whole_platform_or_not',
        '在本机构是否持有债券型基金':'bond_fund_held_in_this_institution_or_not',
        '在本机构是否持有混合型基金':'hybrid_fund_held_in_this_institution_or_not',
        '在本机构是否购买债券型基金':'bond_fund_bought_in_this_institution_or_not',
        '在本机构累计交易笔数':'num_of_transactions_in_this_institution',
        '在全平台是否持有FOF基金':'FOF_held_in_whole_platform_or_not',
        '在本机构是否持有股票型基金':'stock_fund_held_in_this_institution_or_not'
    }

    # 当前用户分类
    user_tag_list = result['yesterday']
    for userType in user_tag_list:
        userTypeName = str(userType['tag'])
        headers.append('userTag_' + userTypeName)
        data_list.append(userType['title'])
        headers.append('userTag_' + userTypeName + '_description')
        data_list.append(userType['description'])
        headers.append('userTag_' + userTypeName + '_count')
        data_list.append(userType['cnt'])
        userTypeDistributed_list = userType['distributed']
        for userTypeDistributed in userTypeDistributed_list:
            userTypeDistributedIndex = str(userTypeDistributed_list.index(userTypeDistributed))
            headers.append('userTag_' + userTypeName + '_distributed' + userTypeDistributedIndex)
            data_list.append(userTypeDistributed['title'])
            headers.append('userTag_' + userTypeName + '_distributed' + userTypeDistributedIndex + '_count')
            data_list.append(userTypeDistributed['from_cnt'])

    # 30天前用户分类
    user_tag_list = result['thirty']
    for userType in user_tag_list:
        userTypeName = str(userType['tag'])
        headers.append('userTag30d_' + userTypeName)
        data_list.append(userType['title'])
        headers.append('userTag30d_' + userTypeName + '_description')
        data_list.append(userType['description'])
        headers.append('userTag30d_' + userTypeName + '_count')
        data_list.append(userType['cnt'])
        userTypeDistributed_list = userType['distributed']
        for userTypeDistributed in userTypeDistributed_list:
            userTypeDistributedIndex = str(userTypeDistributed_list.index(userTypeDistributed))
            headers.append('userTag30d_' + userTypeName + '_distributed' + userTypeDistributedIndex)
            data_list.append(userTypeDistributed['title'])
            headers.append('userTag30d_' + userTypeName + '_distributed' + userTypeDistributedIndex + '_count')
            data_list.append(userTypeDistributed['from_cnt'])
    time.sleep(2)
    driver.back()
    time.sleep(3)

    url_base = 'https://wshop.alipay.com/api/dauUserAnalysis?date=' + dateForUrl + '&version=all&tag='
    tags = ['TY1','TY2','TY3','ZX','GJZ','YJ','LS']
    for tag in tags:
        url = url_base + tag
        driver.get(url)
        html_str = driver.page_source
        pattern = re.compile(r'<pre.+?(?<=>)(.+?)(?=<)')
        result = re.search(pattern, html_str)
        result_json = result.group(1)
        result = json.loads(result_json)
        userTag = result['defaultTag']
        # 通用画像
        tag_head = 'userTag_' + userTag + "_common_"
        common_personas = result['common']
        for persona in common_personas: # persona是common字典下的键 遍历 中文
            for choice in common_personas[persona]:
                if persona in translate_dict and choice['value'] in translate_dict: # 翻译后放入headers
                    headers.append(tag_head + translate_dict[persona] + '_' + translate_dict[choice['value']])
                    data_list.append(choice['cnt'])
                else:
                    print('error, common字典条目缺失:' + persona)
                    print('error, common字典条目缺失:' + choice['value'])
        # 个性画像
        tag_head = 'userTag_' + userTag + "_identity_"
        identity_personas = result['identity']
        for persona in identity_personas:  # persona是idnetity字典下的键 遍历 中文
            for choice in identity_personas[persona]:
                if persona in translate_dict and choice['value'] in translate_dict:  # 翻译后放入headers
                    headers.append(tag_head + translate_dict[persona] + '_' + translate_dict[choice['value']])
                    data_list.append(choice['cnt'])
                else:
                    print('error, identity字典条目缺失:' + persona)
                    print('error, identity字典条目缺失:' + choice['value'])
        time.sleep(2)
        driver.back()
        time.sleep(3)




    with open('data/user_persona.csv', 'w', encoding='gbk', newline='') as fp:  # utf-8编码会有乱码
        writer = csv.writer(fp)
        # writer.writerow(headers)
        writer.writerow(data_list)
        fp.close()




if __name__ == '__main__':
    main()
