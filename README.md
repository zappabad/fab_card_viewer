# FAB Card Viewer

## Table of Contents
1. [Overview] (#overview)
2. [Environment Setup for Python Dummies] (#environment-setup-for-python-dummies)
3. [First Time Setup] (#first-time-setup)
4. [Updating New Cards] (#updating-new-cards)
5. [Contributing] (#contributing)



## Overview
This is a simple card viewer for Flesh and Blood used to aid in video-editing and live production made in Python by Gabriel Singh Bruno (**Ssilhouette#3160** on Discord).

FAB Card Viewer was made so I could record FAB gameplay videos for YouTube while having a card overlay that I could change on demand, that way I could simply upload the recorded file straight to YouTube without needing to edit in the cards talked about in the video after recording.

You can see it in action over at our YouTube channel **Contador na Tunic,** a portuguese FAB channel made by me and my cousin Matheus Singh.
Link to our channel: https://www.youtube.com/@contador-na-tunic
Here's a video showing it on the left side: https://youtu.be/WZfAHRUX2tI?t=299

*Feel free to use FAB Card Viewer for anything you might need, but donations are welcome! Just message me on Discord at Ssilhouette#3160*


## Environment Setup for Python Dummies
1. After cloning the repo, make sure you have Python installed and a *venv* created at the downloaded folder.
2. Open up a command prompt terminal at the folder and run `python -m venv .venv`. This will create a virtual environment (or *venv*) called `.venv`.
3. Open up a PowerShell terminal at the folder and run the following command to activate your *venv*: `.\.venv\Scripts\Activate.ps1`

If you then see the words `(.venv)` at the start of every line, then you have successfully created a *venv* called `.venv` and have successfully activated it, and you should now be good to go to first time setup.

## First Time Setup
The following commands assume you are inside a *venv* called `.venv` PowerShell terminal in the root folder of the repo:

1. Download all requirements. (`python -m pip install -r requirements.txt`)
2. Run `new_cards.py`. This downloads all card data from fabdb.net to data/data.json. (`python new_cards.py`)
3. Run `img_downloader.py`. This will take awhile to complete, as it downloads all cards images from fabdb.net to data/card_images. (`python img_downloader.py`)

After you've downloaded all images, you should now be good to simply run `main.py` and the card viewer should work! (`python main.py`)

## Updating New Cards
Whenever a new set comes out and is properly put into fabdb.net, simply repeat steps 2 and 3 of the First Time Setup to download new card data and images. You won't have to download images of the cards you already have, so it should be faster than first time setup!

## Contributing
I haven't had much time to work on the project in a while, but if you want to contribute to the project, here are a few ideas, but, of course, feel free to come up with your own!

1. Adding support to different transition effects instead of just having fade in/out.
2. Polishing up the list view to not reset back to the top once you select a card.
3. Converging the funcionalities of `new_cards.py` and `img_downloader.py` to be buttons on the `main.py` interface instead of being 3 separate files.
4. **(Big Future Overhaul)** Making FAB Card Viewer support voice-recognition to pull up card images. This is akin to what Team Covenant has, and I believe should be doable to train without having to use any big paid voice-recon APIs.
5. Cleaning up spaghetti code (there's plenty!)