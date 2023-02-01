import requests
import json
import os


data = True
page_num = 1
card_list = []
per_page = 100


while data:
    try:
        r = requests.get('https://api.fabdb.net/cards', params={'page': page_num, 'per_page': per_page})

        print(f'Successfully requested data from FABDB page {page_num}, getting {per_page} cards per page.')
        page_num = page_num + 1
        response = r.json()
        if not response['data']:
            data = False
        else:
            for cards in response['data']:
                card_list.append(cards)
    except:
        page_num = page_num+1


dir_path = os.getcwd()
data_file = dir_path + "/data/data.json"
a_file = open(data_file, "w")
json.dump(card_list, a_file)
a_file.close()