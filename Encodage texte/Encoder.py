# -*- coding: utf-8 -*-
#fonctions
def ouvrir_fichier(nom_fichier_txt):
    with open(nom_fichier_txt) as fobj:
        message=fobj.read()
    return message

def encoder(message):
    message_codé=int.from_bytes(message.encode(), 'big')
    message_codé=conv_bse6(message_codé)
    return message_codé

def conv_bse6(mess_bse_10):   #convertir en base 6 pour gagner de l'espace
    mess_bse_6 = ""
    while mess_bse_10>0:
        reste=mess_bse_10%6
        mess_bse_6=str(reste)+mess_bse_6
        mess_bse_10=mess_bse_10//6
    return mess_bse_6

#principal
message=ouvrir_fichier("message_à_encoder.txt")
message_codé=encoder(message)
print(message_codé)