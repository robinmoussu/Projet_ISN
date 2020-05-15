# -*- coding: utf-8 -*-
from PIL import Image

#fonctions
def décoder(message_codé):
    message_codé=int(message_codé, 6)
    message_décodé=message_codé.to_bytes((message_codé.bit_length() + 7) // 8, 'big').decode()
    return message_décodé

def enregistrer(message):
    with open("message_décodé.txt", "w") as f:
        f.write(message)

def récupérer_message():
    message_codé=""
    for k in range(2):
        for x in range(l):
            for y in range(h):
                p=im1.getpixel((x,y))
                nombre=p[k]
                nombre=renvoyer_bit_faible(nombre)
                message_codé=(message_codé+str(nombre))  
    return message_codé

def renvoyer_bit_faible(nombre):
    if(nombre>=100):
        nombre=str(nombre)
        nombre2=nombre[2]
    elif(nombre>=10):
        nombre=str(nombre)
        nombre2=nombre[1]
    else:
        nombre=str(nombre)
        nombre2=nombre[0]
    return int(nombre2)

#principal
im1 = Image.open("image_sortie.bmp")
l, h=im1.size

message_codé=récupérer_message()
         
clé=int(input("Entrer le code"))
message_codé=message_codé[0:clé]
print(message_codé)

message=décoder(message_codé)
print(message)
enregistrer(message)