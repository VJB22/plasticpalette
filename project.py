# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:26:04 2022

@author: baroc
"""
# make sure everything is saved into the same file (the pictures, the script, everything)
# scrape images from pexels
from pexels_api import API
from colorthief import ColorThief
import matplotlib.pyplot as plt
from skimage.io import imread_collection

# Type your Pexels API
PEXELS_API_KEY = 'GET YOUR OWN API VIA PEXELS WEBSITE'
# Create API object
api = API(PEXELS_API_KEY)
# Search 'pastic waste' photos
api.search('plastic waste', page=20, results_per_page=80)
# Get photo entries
photos = api.get_entries()
# Python List Comprehensions: list to get jpeg images
jpeg_lst = list(map(lambda photo: photo.original, photos))

# dowload all images **run it only once**
# for jpeg in jpeg_lst:
#     response = requests.get(jpeg)
#     file = open("sample_image.jpeg", "wb")
#     file.write(response.content)
#     file.close()

# call images into a temporary dir
col_dir = 'pexels-photo*.jpeg'
# creating a collection with the available images
col = imread_collection(col_dir)
# get images and save into img_lst
img_lst = col._files
# get the 6 dominant colours from all images
for img in img_lst:
    # create colour object
    cl = ColorThief(img)
    # create 5 color palette
    palette = cl.get_palette(color_count=6)
    # plot colors
    plt.imshow([[palette[i] for i in range(6)]])
    plt.show()
    # get plots without labels
    plt.axis('off')
