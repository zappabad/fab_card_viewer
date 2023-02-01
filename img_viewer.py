import PySimpleGUI as sg
from card_funcs import card_json, image_path
from PIL import Image
import io


cards = card_json()

names = []
for card in cards:
    names.append(card['identifier'])


search_list = [[
    sg.Frame('Search for a Card', layout =
    [[sg.Input(do_not_clear=True, size=(34,1),enable_events=True, key='_INPUT_')],
                                                        [sg.Listbox(names, size=(34,42), select_mode=3,enable_events=True, highlight_background_color="Black", key='_LIST_')
    ]])
]]

col1 = sg.Column(search_list)

# First the window layout in 2 columns
layout = [[
    col1
]]



