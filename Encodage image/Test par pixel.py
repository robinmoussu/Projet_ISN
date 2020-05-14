# -*- coding: utf-8 -*-
from PIL import Image

im1 = Image.open("image_sortie.bmp")
p=im1.getpixel((74,74))
print(p)