# -*- coding: utf-8 -*-
from PIL import Image

im1 = Image.open("image_sortie.bmp")
for k in range(20):
    p=im1.getpixel((0,k))
    print(p)

print(jaaj)
p=im1.getpixel((0,2))
print(p)


bit_faible=bit_faible_nul(nombre)
            if bit_faible==0:
                nombre_de_0=nombre_de_0+1
            else:
                nombre_de_0=0
            if nombre_de_0>10:
                print(nombre_de_0)
            if nombre_de_0<50:
                

def bit_faible_nul(nombre):
    if(len(nombre)==3):
        if nombre[2]==0:
            return 0
        else:
            return 1
    elif(len(nombre)==2):
        if nombre[1]==0:
            return 0
        else:
            return 1
    else:
        if nombre==0:
            return 0
        else:
            return 1