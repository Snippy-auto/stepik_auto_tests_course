import json
import pprint

with open('Abracadabra__1_.txt', 'r') as file:
    text = file.read()
    text_decodered = []
    with open('Alphabet.json', 'r') as decoder:
        alphabet = json.load(decoder)
        for line in text:
            for symbol in line:
                if symbol.isalpha():
                    for keys, values in alphabet.items():
                        if keys == symbol:
                            text_decodered.append(values)
                else:
                    text_decodered.append(symbol)
        print(*text_decodered, sep='')
 #    count_women = 0
 #   id = 0
 #   for element in data:
##        id_group = element['id_group']
 #      cnt = 0
 #       for chel in element['people']:
  #          if chel['gender'] == "Female" and chel['year'] > 1977:
 #               cnt += 1
#        if cnt > count_women:
 #           count_women = cnt
 #           id = id_group
 #   print(id, count_women)


