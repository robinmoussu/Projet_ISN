# -*- coding: utf-8 -*-
from PIL import Image

im1 = Image.open("image_sortie.bmp")
p=im1.getpixel((0,101))
print(p)