import json
import os


def card_json():
    f = open('data/data.json', 'r')
    card = json.load(f)
    f.close()
    return card


def url_corrector(cards, identifier):
    for card in cards:
        if identifier == card['identifier']:
            url = card['image'].partition('.png')[0] + '.png'
    return url


def image_path(cards, identifier):
    dir_path = os.getcwd()
    card_images_dir = dir_path + "/data/card_images/"
    path = card_images_dir + identifier + '.png'
    return path
