import json
import pprint

with open('manager_sales.json', 'r') as f:
    f_j = json.load(f)
    manager_n = ''
    manager_l = ''
    maxi = 0
    for data in f_j:

        manager_name = data['manager']['first_name']
        manager_last = data['manager']['last_name']
        total = 0

        for cars in data['cars']:
            total += cars['price']

        if total > maxi:
            maxi = total
            manager_n = manager_name
            manager_l = manager_last

    print(f'{manager_n} {manager_l} {maxi}')