import json
import pprint

with open('group_people.json', 'r') as file:
    data = json.load(file)
    count_women = 0
    id = 0
    for element in data:
        id_group = element['id_group']
        cnt = 0
        for chel in element['people']:
            if chel['gender'] == "Female" and chel['year'] > 1977:
                cnt += 1
        if cnt > count_women:
            count_women = cnt
            id = id_group
    print(id, count_women)


