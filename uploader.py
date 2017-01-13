import os, sys
from PIL import Image

def resize_file(file, size):
    im = Image.open(file)
    width, height = im.size
    newsize = get_size(width, height, size)
    im.thumbnail(newsize, Image.ANTIALIAS)
    return im

def get_size(width, height, size):
    if width >= height:
        return [size, size]
    divby = width / size
    new_size= int(height / divby)
    return [new_size, new_size]

fullsize = 1080
thumb_size = 200

imagedir = os.path.join(os.getcwd(), 'swainerimages')
source_path = os.path.join(imagedir, 'source')
files = os.scandir(source_path)
image_path = os.path.join(imagedir, 'images')
thumb_path = os.path.join(imagedir, 'thumbs')

for file in files:
    thumb = resize_file(file.path, thumb_size)
    thumb_name = os.path.join(thumb_path, file.name)
    thumb.save(thumb_name)
    full_image = resize_file(file.path, fullsize)
    full_image_name = os.path.join(image_path, file.name)
    full_image.save(full_image_name)
