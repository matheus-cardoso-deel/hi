import os, Image

ALLOWED_EXTENSIONS = set(['jpeg', 'jpg'])

def resize_to_icon_size(filename):
	img_path = os.path.join('app/uploads/users/icons/', filename)
	img = Image.open(img_path)
	img.resize((32,32), Image.ANTIALIAS).save(img_path)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS