#!/usr/bin/env python
# encoding: utf-8
"""
resizeImages.py

Created by Maksim Surguy on 2012-04-08.
http://maxoffsky.com

modified by Freddy Limpens on march 24, 2017

"""

import os

from PIL import Image, ImageOps


def ensure_dir(f):
    """ check dir at path f exists and create it if not"""
    if not os.path.exists(f):
        os.makedirs(f)

def main():
    
    # set max image dimensions
    max_width = 1000
    max_height = 800

    # set thumbnail size
    thumb_size = (240, 150)

    # optional - set the folder names if different names needed
    photo_source_folder = "media"
    source_folder = os.path.join(os.getcwd(), photo_source_folder)
    output_big_folder = os.path.join(source_folder,"pics")
    output_thumb_folder = os.path.join(source_folder,"thumbs")
    #ensure_dir(output_big_folder)
    ensure_dir(output_thumb_folder)

    dirList = [fname for fname in os.listdir(source_folder)
                     if fname.lower().endswith(".png") or fname.lower().endswith(".jpg")]
    for fname in dirList:
        image = Image.open(os.path.join(source_folder,fname))
        #print "Resizing %s" % fname
        # If already smaller than target size, copy as is
        # if image.size[0] <= 640 and image.size[1] <= 400:
        #     image.save(os.path.join(output_big_folder,fname), quality = 92)
        # else:
        #     image_big = image.copy()
        #     image_big.thumbnail((max_width, max_height), Image.ANTIALIAS)
        #     image_big.save(os.path.join(output_big_folder,fname), quality = 92)
        # generate thumbnails    
        print "Thumbnailing %s" % fname
        thumbnail = ImageOps.fit(image, thumb_size, Image.ANTIALIAS)
        thumbnail.save(os.path.join(output_thumb_folder,fname), quality = 90)
             

if __name__ == '__main__':
    main()
