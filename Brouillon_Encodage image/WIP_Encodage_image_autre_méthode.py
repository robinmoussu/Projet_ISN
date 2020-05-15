# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np

#fonctions
def ouvrir_fichier(nom_fichier_txt):
    with open(nom_fichier_txt) as fobj:
        message=fobj.read()
    return message

def encoder(message):
    message_codé=int.from_bytes(message.encode(), 'big')
    message_codé=conv_bse6(message_codé)
    return str(message_codé)

def conv_bse6(mess_bse_10):   #convertir en base 6 pour gagner de l'espace
    mess_bse_6 = ""
    while mess_bse_10>0:
        reste=mess_bse_10%6
        mess_bse_6=str(reste)+mess_bse_6
        mess_bse_10=mess_bse_10//6
    return mess_bse_6

def créer_grande_matrice():
    l_gm=(3*l) #longueur grande matrice
    h_gm=(3*h) #largeur grande matrice
    grande_matrice=np.zeros((l_gm,h_gm), dtype=int)
    for x in range(l):
        for y in range(h):
            p=im1.getpixel((x,y))
            for k in range(2):
                grande_matrice[x,y]=p[k]
    return grande_matrice,l_gm,h_gm

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

def matrice(couleur):
    matrice_sortie=np.zeros(im1.size, dtype=int)
    for y in range(h):
        for x in range(couleur,(l_gm-1),9):
            print(x)
            print(y)
            matrice_sortie[x,y]=grande_matrice[x,y]
    return matrice_sortie

#principal
message=ouvrir_fichier("message_à_encoder.txt")
message_codé=encoder(message)
print("La clé pour décoder le message secret est :", len(message_codé))

im1 = Image.open("image.bmp")
l, h=im1.size
cap=((l*h)*3)  #capacité de l'image

if (len(message_codé)>cap):
    print("Erreur : le message est trop long")
else:
    grande_matrice,l_gm,h_gm=créer_grande_matrice()
    matrice_r=matrice(0)  
    matrice_g=matrice(1)
    matrice_b=matrice(2)

    im2 = Image.new("RGB",(l,h))
    for x in range(l):
        for y in range(h):
            r=matrice_r[x,y]
            g=matrice_g[x,y]
            b=matrice_b[x,y]
            im2.putpixel((x,y),(r,g,b))
    im2.save('image_sortie.bmp')