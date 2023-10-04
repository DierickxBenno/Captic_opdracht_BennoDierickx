# from PIL import Image # can be useful when working with Images
import json
import cv2
import glob
import numpy as np

class JSONify:
	def __init__(self, path_to_pictures="../data/pictures/"):
		self.path = path_to_pictures
		self.size = 2**7
		self.names = []
		self.get_all_image_names()


	def JSONify_picture(self, name):
		# fetch picture from path
		pic = cv2.imread(f"{self.path}{name}.jpg")
		split_name = name.split("_")
		kind = split_name[0]
		# resize picture
		resized_pic = cv2.resize(pic, (self.size, self.size))
		metadata = {"kind": kind, "picture": resized_pic.tolist()}
		metadata = self._make_pixel_colums(metadata)
		return metadata

	# works locally
	def get_all_image_names(self):
		pictures = r"*" # * means all in regex
		image_names = []
		for pic in glob.glob(f"{self.path}{pictures}"):
			# because pic is formatted in a certain way we could also just use indexing on the string
			pic = pic[len(self.path) : -4]  # likely not the best way to do this
			image_names.append(pic)

		self.names = image_names

	def write_to_json(self):
		# get all names
		names = self.names
		# load all
		data = []
		for name in names:
			image_meta = self.JSONify_picture(name)
			data.append(image_meta)

		with open(f"images.json", "w") as f:
			json.dump(data, f)

# avoid unwanted execution when imported, this is a test script
# if __name__ == "__main__": # this works
# 	converter = JSONify()
# 	# load all
# 	names = get_all_image_names()

# 	for name in names:
# 		image_meta = JSONify_picture(name)
# 		print(image_meta["kind"])
# 		print(len(image_meta["picture"]))

# 	# check if all names are loaded
# 	print(len(converter.names))

# 	# load random
# 	random_name = np.random.choice(converter.names)
# 	random_image = converter.JSONify_picture(random_name)
# 	print(random_image["kind"])

if __name__ == "__main__":
	converter = JSONify()
	converter.write_to_json()