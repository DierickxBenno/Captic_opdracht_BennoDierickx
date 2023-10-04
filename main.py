import json
import cv2

pic_path = ""

def JSONify_picture(name):
	#set size for resize, 2**x to easily chage size
	size = 2**7
	# fetch picture from path
	pic = cv2.imread(f"./data/pictures/{name}.jpg")
	split_name = name.split("_")
	kind = split_name[0]
	# resize picture
	resized_pic = cv2.resize(pic, (size, size))
	metadata = {"kind": kind, "picture": resized_pic.tolist()}
	return metadata

# avoid unwanted execution when imported
if __name__ == "__main__":
	image_meta = JSONify_picture()
	print(image_meta["kind"])
	print(len(image_meta["picture"]))

 