from operation import Operation
import re
import json
import time
import datetime
import csv
# TODO
def main():
    date = (datetime.datetime.now() - datetime.timedelta(days=2))
    dateForUrl = date.strftime("%Y%m%d")
    date = date.strftime("%Y-%m-%d")
    op = Operation()
    driver = op.driver





if __name__ == '__main__':
    main()
