from PIL import Image
import os, sys

path = "C:\\Users\\abhay\\Desktop\\NORMALIZED_IMAGES\\"
path1= "C:\\Users\\abhay\\Desktop\\nsd1\\"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path1+item)
            imResize = im.resize((180,180), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)


resize()