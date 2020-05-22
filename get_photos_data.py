# this file does NOT generate the 'total' row with all of the data summed and combined

import os
import math

def generate_markdown_cols(cols):
	return " | ".join(cols).strip() + "\n"

def get_filesize_in_kb(filepath):
	BYTES_PER_KB = 1000;
	return round(os.path.getsize(filepath) / BYTES_PER_KB, 2)

def get_heic_and_jpg_filepaths(image_title):
	image_title = str(image_title)
	return [ "./heic/" + image_title + ".heic", "./jpg/" + image_title + ".jpg" ]

col_titles = ["Filename", ".HEIC size (kb)", ".JPG size (kb)", ".HEIC:.JPG size ratio", ".HEIC size reduction from .JPG"]

final_markdown = generate_markdown_cols(col_titles)
final_markdown += generate_markdown_cols(["---"] * len(col_titles))

# this constant should be changed if the size 'images' list in 'get_photos.py' is changed
# it may have been better to move the images list to a separate file, although that is (in my opinion) beyond the scope of this basic program
image_count = 500

# note: image titles start at 1
for image_title in range(1, image_count + 1):
	image_filepaths = get_heic_and_jpg_filepaths(image_title)
	heic_size = get_filesize_in_kb(image_filepaths[0])
	jpg_size = get_filesize_in_kb(image_filepaths[1])
	heic_jpg_ratio = round(heic_size / jpg_size, 2);

	final_markdown += generate_markdown_cols([
		"**`" + str(image_title) + "`** [`.heic`](./heic/" + str(image_title) + ".heic)/[`.jpg`](./jpg/" + str(image_title) + ".jpg)",
		str(heic_size) + " kb",
		str(jpg_size) + " kb",
		str(heic_jpg_ratio),
		str(round((1 - heic_jpg_ratio) * 100)) + "%"
	])

print(final_markdown)