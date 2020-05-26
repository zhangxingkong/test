import json
import time
from pprint import pprint

with open('test', 'r', encoding='gbk') as f:
    json_data = f.read()

dict_data = json.loads(json_data)
pprint(dict_data)
k_list = list(dict_data.keys())
# print(k_list)
crawl_time = time.strftime('%Y-%m-%d %H:00:00', time.localtime())
item_list = []
user_item_list = []
for i in k_list:
    if i == 'common' or i == 'identity':
        for k in list(dict_data[i].keys()):
            for m in dict_data[i][k]:
                item = {}
                item['index'] = k
                item['data_type'] = m['value']
                item['data_value'] = m['cnt']
                item['user_type'] = 'A类体验用户'
                item['crawl_time'] = crawl_time
                print(item)
                item_list.append(item)
    elif i == 'yesterday':
        for j in dict_data[i]:

            for n in j['distributed']:
                user_item = {}
                user_item['user_type'] = j['title']
                user_item['crawl_time'] = crawl_time
                user_item['total_count'] = j['cnt']
                # component_item = {}
                # component_item['component'] = n['title']
                # component_item['count'] = n['from_cnt']
                user_item['component'] = n['title']
                user_item['component_count'] = n['from_cnt']
                user_item['rate'] = '%.2f%%' % (100 * user_item['component_count'] / user_item['total_count'])
                user_item_list.append(user_item)

            # for c_item in component_item_list:
            #     user_item['component'] =

total_counts = {}
for item in item_list:
    try:
        total_counts[item['index']] += item['data_value']
    except:
        total_counts[item['index']] = item['data_value']

print(total_counts)

for item in item_list:
    rate = item['data_value'] / total_counts[item['index']]
    data_rate = '%.2f%%' % (rate * 100)
    item['data_rate'] = data_rate
    print(item)

for user_item in user_item_list:
    print(user_item)
