import PySimpleGUI as sg
import cv2
import numpy as np
from img_viewer import layout, names, cards
from card_funcs import image_path
from time import sleep
import json
import os


dir_path = os.getcwd()
data_file = dir_path + "/variables.json"

with open(data_file, 'r') as file:
    variables = json.load(file)


window = sg.Window('FAB Card Viewer', layout, resizable=True, finalize=True)
lastcard = image_path(cards, 'eye-of-ophidia')
# Create an event loop
while True:

    event, values = window.read()

    if event is None or event == 'Exit':                # always check for closed window
        break
    if values['_INPUT_'] != '':                         # if a keystroke entered in search field
        search = values['_INPUT_']
        new_values = [x for x in names if search.lower() in x.replace('-', ' ').lower()]  # do the filtering
        window.Element('_LIST_').Update(new_values)     # display in the listbox
    else:
        window.Element('_LIST_').Update(names)
    if event == '_LIST_' and len(values['_LIST_']):     # if a list item is chosen--
        img1 = cv2.imread(lastcard, cv2.IMREAD_COLOR)
        img1 = cv2.resize(img1, (round(variables["card_zoom_level"]*546), round(variables["card_zoom_level"]*762)), interpolation=cv2.INTER_AREA) #resizing for lower res cards

        img2 = cv2.imread(image_path(cards, values['_LIST_'][0]), cv2.IMREAD_COLOR)
        img2 = cv2.resize(img2, (round(variables["card_zoom_level"]*546), round(variables["card_zoom_level"]*762)), interpolation=cv2.INTER_AREA)
        for i in np.linspace(0, 1, variables["number_of_steps"]):
            alpha = i
            beta = 1 - alpha
            output = cv2.addWeighted(img2, alpha, img1, beta, 0)
            cv2.imshow('Card Images', output)
            sleep(variables["time_between_steps"])
            if cv2.waitKey(1) == 27:
                break
        lastcard = image_path(cards, values['_LIST_'][0])





