import os, Image

def resize_to_icon_size(filename):
	img_path = os.path.join('app/uploads/users/icons/', filename)
	img = Image.open(img_path)
	img.resize((32,32), Image.ANTIALIAS).save(img_path)