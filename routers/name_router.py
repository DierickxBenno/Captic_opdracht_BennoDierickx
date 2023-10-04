paths_to_modules = ["../metadata"]
from fastapi import APIRouter, HTTPException
import json
import sys

import sys

for path in paths_to_modules:
	if path not in sys.path:
		sys.path.append(path)

from metadata.jsonify import JSONify

converter = JSONify("./data/pictures/")


def get_image(name):
	image_meta = converter.JSONify_picture(name)
	return image_meta


def get_all_image_names():
	names = converter.names
	return names


router = APIRouter(
	prefix="/local/images",
	tags=["Image"],
	responses={400: {"Image": "Not found"}},
)


@router.get("/{name}")
def get_image_by_name(name: str):
	image = get_image(name)
	if image is None:
		raise HTTPException(status_code=404, detail="Image not found")
	return image


@router.get("/")
def get_all_images():
	# images = []
	names = get_all_image_names()
	if len(names) == 0:
		raise HTTPException(status_code=404, detail="No images found")

	return names
