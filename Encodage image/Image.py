# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np

#fonctions
def remplacer_bit_faible(nombre, compteur):
    if(nombre>100):
        nombre=str(nombre)
        nombre2=(nombre[0]+nombre[1]+message_codé[compteur])
    elif(nombre>10):
        nombre=str(nombre)
        nombre2=(nombre[0]+message_codé[compteur])
    else:
        nombre=str(nombre)
        nombre2=(message_codé[compteur])
    return int(nombre2)

def matrice(couleur,compteur):
    matrice_sortie=np.zeros(im1.size, dtype=int)
    for x in range(l):
        for y in range(h):
            p=im1.getpixel((x,y))
            p2=remplacer_bit_faible(p[couleur],compteur)
            compteur=compteur+1
            matrice_sortie[x,y]=p2
    return compteur,matrice_sortie

#principal
message_codé="131311351425042412305024012545011210225555440342240014245242443323551122021213311233253501210115454153"

im1 = Image.open("image.bmp")
l, h=im1.size
cap=((l*h)*3)
print("La capacité de stockage de l'image est de :",cap,"bits")
print("Le message pèse :",len(message_codé),"bits")
if (len(message_codé)>cap):
    print("Erreur : le message est trop long")
else:
    for k in range(cap-len(message_codé)):
        message_codé=(message_codé+"0")
compteur=0
compteur,matrice_r=matrice(0,compteur)
compteur,matrice_g=matrice(1,compteur)
compteur,matrice_b=matrice(2,compteur)

im2 = Image.new("RGB",(l,h))
for x in range(l):
    for y in range(h):
        r=matrice_r[x,y]
        g=matrice_g[x,y]
        b=matrice_b[x,y]
        im2.putpixel((x,y),(r,g,b))
im2.save('image_sortie.bmp')