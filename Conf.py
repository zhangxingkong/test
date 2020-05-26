XPATH = {
    'homepage': {
        'login_xpath': '//a[@class="btn-login"]',
        'login_way_xpath': '//li[text()="账密登录"]'
    },
    'rank_menu': {
        'drop_down_xpath': '//span[@class="ant-select-arrow"]',
        '曝光UV日排名': '//ul[@role="menu"]/li[1]',
        '曝点率日排名': '//ul[@role="menu"]/li[2]',
        '人均点击数日排名': '//ul[@role="menu"]/li[3]',
        '曝转率日排名': '//ul[@role="menu"]/li[4]',
        '次日回访率排名': '//ul[@role="menu"]/li[5]',
        '七日回访率排名': '//ul[@role="menu"]/li[6]',
        '通用服务曝光UV排名': '//ul[@role="menu"]/li[7]',
        '场景页曝光UV排名': '//ul[@role="menu"]/li[8]',
        '场景页曝点率排名': '//ul[@role="menu"]/li[9]',
        '通用服务曝点率排名': '//ul[@role="menu"]/li[10]',
        '周曝光UV排名': '//ul[@role="menu"]/li[11]',
        '陪伴页停留时长排名': '//ul[@role="menu"]/li[12]',
        '陪伴月度评分排行': '//ul[@role="menu"]/li[13]',
    },
    'main_menu': {
        '运营总览': '//a[text()="运营总览"]',
        '营销活动': '//a[text()="营销活动"]',
        '流量分析': '//a[text()="流量分析"]',
        '交易分析': '//ul[@id="analyze$Menu"]//a[text()="交易分析"]',
        '内容分析': '//a[text()="内容分析"]',
        '活动对账': '//a[text()="活动对账"]',
        '服务分析': '//a[text()="服务分析"]',
        '交易分析_2': '//ul[@id="op$Menu"]//a[text()="交易分析"]',
        '活动分析': '//a[text()="活动分析"]',
        '平台招商': '//a[text()="平台招商"]',
        '交易渠道分析': '//a[text()="交易渠道分析"]',
        '新版阵地流量': '//a[text()="新版阵地流量"]'
    },
    'sub_menu': {
        '数据概览': '//div[text()="数据概览"]',
        '排名指标': '//div[text()="排名指标"]',
        '权益活动': '//div[text()="权益活动"]',
        '菜单栏': '//div[text()="菜单栏"]',
        '产品列表': '//div[text()="产品列表"]',
        '图文展位': '//div[text()="图文展位"]',
        '基金立减红包': '//div[text()="基金立减红包"]',
        '基金定投礼包': '//div[text()="基金定投礼包"]',
        '财运金': '//div[text()="财运金"]',
        '场景包装': '//div[text()="场景包装"]',
        '平台陪伴': '//div[text()="平台陪伴"]',
        '通用服务': '//div[text()="通用服务"]',
        '未外透': '//div[text()="未外透"]',
        '近半年': '//span[text()="近半年"]',
        '近30天': '//span[text()="近30天"]',
        '申购': '//div[text()="申购"]',
        '定投': '//div[text()="定投"]',
        '区块概览': '//div[text()="区块概览"]',

    },
    'campaign_acc': {
        'btn_xpath': '//button[@class="ant-btn campaign-download-btn"]',
        'drop_down_xpath': '//div[@class="ant-col-18 ant-form-item-control-wrapper"]//span[@class="ant-select-arrow"]'
    },
    'campaign_sheet': [
        '/html/body/div[3]/div/div/div/ul/li[1]',
        '/html/body/div[3]/div/div/div/ul/li[2]',
        '/html/body/div[3]/div/div/div/ul/li[3]',
        '/html/body/div[3]/div/div/div/ul/li[4]',
        '/html/body/div[3]/div/div/div/ul/li[5]',
        '/html/body/div[3]/div/div/div/ul/li[6]',
        '/html/body/div[3]/div/div/div/ul/li[7]',
        '/html/body/div[3]/div/div/div/ul/li[8]',
        '/html/body/div[3]/div/div/div/ul/li[9]',
        '/html/body/div[3]/div/div/div/ul/li[10]',
        '/html/body/div[3]/div/div/div/ul/li[11]',
        '/html/body/div[3]/div/div/div/ul/li[12]'
    ],
    'download': {
        'camp_download_xpath': '//button[@class="ant-btn ant-btn-primary ant-btn-lg"]',
    },
    'frame': '//div//iframe',
    'flow_menu': {
        'drop_down_xpath': '//span[@class="ant-select-arrow"]',
        '整体': '//ul[@role="menu"]/li[1]',
        '首页': '//ul[@role="menu"]/li[2]',
        '场景包装': '//ul[@role="menu"]/li[3]',
        '平台陪伴': '//ul[@role="menu"]/li[4]',
        '通用服务': '//ul[@role="menu"]/li[5]',
        'download': '//button[@class="ant-btn"]',
        'download2': '//button[@class="ant-btn"]/span[text()="下 载"]/..',
    },
    'content_aly': {
        'download_1': '//div[@class="ant-tabs-content"]/div/div[1]//button',
        'download_2': '//div[@class="ant-tabs-content"]/div/div[2]//button',
        'download_3': '//div[@class="ant-tabs-content"]/div/div[3]//button',
        'download_4': '//div[@class="ant-tabs-content"]/div/div[4]//button'
    },
    'account': {
        # 'download_1': '//div[@class="ant-tabs-content"]/div/div[1]//button',
        'download_1': '//span[text()="下 载"]/parent::button',
        # 'download_2': '//div[@class="ant-tabs-content"]/div/div[2]//button'
        # 'download_2': '//button[2]//span[text()="下 载"]/parent::button'
        'download_2': '//div[@class="ant-tabs-content ant-tabs-content-animated"]/div[2]//button',
        'download_3': '//div[@class="ant-tabs-tabpane ant-tabs-tabpane-active"]/div/div[1]/button',
    },
    'service_aly': {
        'download_1': '//div[@class="ant-tabs-content"]/div/div[1]//button',
        'download_2': '//div[@class="ant-tabs-content"]/div/div[2]//button',
        'download_3': '//div[@class="ant-tabs-content"]/div/div[3]//button',
        'download_4': '//div[@class="ant-tabs-content"]/div/div[4]//button',
        'download_5': '//div[@id="react-content"]//div[text()="当日交易核心数据看板"]/..//button/span[text()="下 载"]/..',
        'frame_2': '//div[@class="ant-row"]//iframe[@id="myreports-overviewOp"]',
        'download_5_2': '//div[@id="react-content"]//div[text()="当日运营数据看板"]/..//button/span[text()="下 载"]/..',
        'download_6': '//div[@class="ant-row"]/div[1]//button/span[text()="下载数据"]/..',
        'download_7': '//div[@class="ant-modal-body"]//button',
    },
    'platform_invest': {
        'download_1': '//div[@class="ant-spin-container"]/div/div/button',

    },
    'trade_aly': {
        'select_xpath': '//div[@class="ant-select-selection__rendered"]'
    },
    'marketing_activity': {
        'next_page': '//li[@title="下一页"]',
        'campaign_status': '//tbody/tr/td[6]',
        'check': '//tbody/tr/td[9]//span[@class="operation-btn check-btn"]'
    },
    'position_flow': {
        'see_details': '//div[@data-engine-root="true"]/a[text()="查看详情"]',
        'download_1': '//div[@role="tabpanel" and @aria-hidden="false"]//button/span[text()="下 载"]/parent::button',
    },
}

ID_XPATH = {
    'login': {
        'acc_xpath': 'J-input-user',
        'pwd_xpath': 'password_rsainput',
        'img_xpath': 'J-checkcode-img',
        'code_xpath': 'J-input-checkcode',
        'login_bt_xpath': 'J-login-btn'
    }
}

EXPORT_FILE = {
    'ranking_export_file': 's_sp_alipay_ranking',
    'configure_export_file': 's_sp_alipay_campaign_configure',
    'traffic_export_file': 's_sp_alipay_traffic',
    'trade_export_file': 's_sp_alipay_trade',
    'equity_campaign_export_file': 's_sp_alipay_content_campaign',
    'menu_traffic_export_file': 's_sp_alipay_content_menu_traffic',
    'fundlist_export_file': 's_sp_alipay_content_fundlist',
    'pic_traffic_export_file': 's_sp_alipay_content_pic_traffic',
    'scene_export_file': 's_sp_alipay_service_scene',
    'platform_export_file': 's_sp_alipay_service_platform',
    'common_export_file': 's_sp_alipay_service_common',
    'unrelease_export_file': 's_sp_alipay_service_unrelease',
    'campaign_export_file': 's_sp_alipay_campaign',
    'account_export_file': 's_sp_alipay_statement'
}

TASK_LIST = {
    'task_operation': (
        {'ranking': (
            # 运营总览 -- 排名指标
            {'click': XPATH['main_menu']['运营总览']},
            {'click': XPATH['sub_menu']['排名指标']},
            {'switch_frame': XPATH['frame']},
            {'click': XPATH['flow_menu']['download2']},
        )},
        # 运营司南 交易分析
        {'trans_analyzing_2': (
            {'quit_frame': None},
            {'click': XPATH['main_menu']['交易分析_2']},
            {'switch_frame': XPATH['frame']},
            {'click': XPATH['service_aly']['download_5']},
            {'click': XPATH['service_aly']['download_6']},
            {'click': XPATH['service_aly']['download_7']},
        )},
        # 运营总览 - 数据概览
        {'data_overview': (
            {'quit_frame': None},
            {'click': XPATH['sub_menu']['数据概览']},
            {'switch_frame': XPATH['frame']},
            {'click': XPATH['service_aly']['download_5']},

            {'quit_frame': None},
            {'switch_frame': XPATH['service_aly']['frame_2']},
            {'roll_down_window': XPATH['service_aly']['download_5_2']},
            {'click': XPATH['service_aly']['download_5_2']},

            {'quit_frame': None},
            {'switch_frame': XPATH['frame']},
            {'roll_up_window': None},
        )},
        # 活动分析
        {'active_analyzing': (
            {'quit_frame': None},
            {'click': XPATH['main_menu']['活动分析']},
            {'switch_frame': XPATH['frame']},
            {'click': XPATH['service_aly']['download_5']},
        )},
        # 活动对账
        {'account': (
            {'quit_frame': None},
            {'click': XPATH['main_menu']['活动对账']},
            {'switch_frame': XPATH['frame']},

            # 超过7天补数使用
            # {'click': XPATH['sub_menu']['近30天']},
            # 超过一个月补数使用
            # {'click': XPATH['sub_menu']['近半年']},

            {'click': XPATH['account']['download_1']},
            {'unzip': None},

            {'click': XPATH['sub_menu']['基金定投礼包']},
            {'click': XPATH['account']['download_2']},
            {'unzip': None},

            {'click': XPATH['sub_menu']['财运金']},
            {'click': XPATH['account']['download_3']},
            {'unzip': None},
        )},
        # 服务分析
        {'service_analyzing': (
            {'quit_frame': None},
            {'click': XPATH['main_menu']['服务分析']},
            {'switch_frame': XPATH['frame']},

            # 超过7天补数使用
            # {'click': XPATH['sub_menu']['近30天']},
            # 超过一个月补数使用
            # {'click': XPATH['sub_menu']['近半年']},

            {'click': XPATH['service_aly']['download_1']},
            {'unzip': None},

            {'click': XPATH['sub_menu']['平台陪伴']},
            {'click': XPATH['service_aly']['download_2']},
            {'unzip': None},

            {'click': XPATH['sub_menu']['通用服务']},
            {'click': XPATH['service_aly']['download_3']},
            {'unzip': None},

            {'click': XPATH['sub_menu']['未外透']},
            {'click': XPATH['service_aly']['download_4']},
            {'unzip': None},

        )},
        # 流量分析
        {'flow_analyzing': (
            {'quit_frame': None},
            {'click': XPATH['main_menu']['流量分析']},
            {'switch_frame': XPATH['frame']},

            # 超过7天补数使用
            # {'click': XPATH['sub_menu']['近30天']},
            # 超过一个月补数使用
            # {'click': XPATH['sub_menu']['近半年']},

            {'click': XPATH['flow_menu']['download']},
            {'unzip': None},

            {'click': XPATH['flow_menu']['drop_down_xpath']},
            {'click': XPATH['flow_menu']['首页']},
            {'click': XPATH['flow_menu']['download']},
            {'unzip': None},

            {'click': XPATH['flow_menu']['drop_down_xpath']},
            {'click': XPATH['flow_menu']['场景包装']},
            {'click': XPATH['flow_menu']['download']},
            {'unzip': None},

            {'click': XPATH['flow_menu']['drop_down_xpath']},
            {'click': XPATH['flow_menu']['平台陪伴']},
            {'click': XPATH['flow_menu']['download']},
            {'unzip': None},

            {'click': XPATH['flow_menu']['drop_down_xpath']},
            {'click': XPATH['flow_menu']['通用服务']},
            {'click': XPATH['flow_menu']['download']},
            {'unzip': None},
        )},

        # 新版阵地流量
        {'position_flow':(
            {'quit_frame': None},

            {'change_windowhandler': 'https://wshop.alipay.com/op-dau-new/默认页面'},
            {'sleep': None},
            {'switch_frame': XPATH['frame']},
            {'click': XPATH['position_flow']['download_1']},

            {'click': XPATH['sub_menu']['区块概览']},
            {'click': XPATH['position_flow']['download_1']},
        )},
        # # {'content_analyzing': (
        #     # 进行增量，获取一天数据
        #     {'increment': None},
        #     {'quit': None}
        # )}

    ),

}
