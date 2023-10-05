# from PIL import Image # can be useful when working with Images
import sys

sys.path.append("/usr/lib/python3.11/site-packages/")  # hard coded solution, for docker environment

import json
import cv2
import glob
import numpy as np


class JSONify:
    def __init__(self, path_to_pictures="./data/pictures/"):
        self.path = path_to_pictures
        self.size = 2**7
        self.names = []
        self.get_all_image_names()

        self.__write_to_json()

    def JSONify_picture(self, name):
        # fetch picture from path
        pic = cv2.imread(f"{self.path}{name}.jpg")
        split_name = name.split("_")
        kind = split_name[0]
        # resize picture
        resized_pic = cv2.resize(pic, (self.size, self.size))
        metadata = {"kind": kind, "picture": resized_pic.tolist()}
        return metadata

    # works locally
    def get_all_image_names(self):
        pictures = r"*"  # * means all in regex
        image_names = []
        for pic in glob.glob(f"{self.path}{pictures}"):
            # because pic is formatted in a certain way we could also just use indexing on the string
            pic = pic[len(self.path) : -4]  # likely not the best way to do this
            image_names.append(pic)

        self.names = image_names

    def __write_to_json(self):
        # get all names
        names = self.names
        # load all
        data = []
        for name in names:
            image_meta = self.JSONify_picture(name)
            data.append(image_meta)
        # print(data)
        # write to json
        with open(f"./metadata/images.json", "w") as outfile:
            # first check if file is empty

            json.dump(data, outfile)

