import requests
from card_funcs import card_json
from tqdm import tqdm
import os
from pathlib import Path

card_data_folder_path = 'data/data.json'

cards = card_json()


dir_path = os.getcwd()
path = dir_path + '/data/card_images/'
print(f"Images being downloaded from fabdb.net, they'll end up in {path}, make sure you have an internet connection!")
print(f"If you see any errors, check that there is a file called data.json inside {dir_path}/data")
for card in tqdm(cards):
    image_url = card['image'].split('.png')[0] + '.png'
    image_name = card['identifier'] + '.png'
    save_to_path = path + image_name
    if os.path.isfile(Path(save_to_path)):
        pass
    else:
        img_data = requests.get(image_url).content
        with open(save_to_path, 'wb') as handler:
            handler.write(img_data)
