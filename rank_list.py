
from operation import Operation
import time

def main():
    op = Operation()
    driver = op.driver
    # op.login('//a[@class="btn-login"]',
    #          '//li[text()="账密登录"]',
    #          'J-input-user',
    #          'password_rsainput',
    #          'J-checkcode-img',
    #          'J-input-checkcode',
    #          'J-login-btn',
    #          '99fund@htffund.com',
    #          'htf99!123'
    #          )

    #input()
    driver.get('https://wshop.alipay.com/api/dashboard/queryAumData')

    html_str = driver.page_source
    # print(html_str)
    # driver.back()
    # driver.get('https://wshop.alipay.com/api/dashboard/queryProductData')
    # html_str = driver.page_source
    # print('###')
    # print(html_str)
    # print()
    op.rank_str_to_csv(html_str)
    time.sleep(2)
    driver.back()
    time.sleep(3)
    #driver.refresh()
    # input()


if __name__ == '__main__':
    main()
