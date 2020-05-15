# -*- coding: utf-8 -*-
#fonctions
def décoder(message_codé):
    message_codé=int(message_codé, 6)
    message_décodé=message_codé.to_bytes((message_codé.bit_length() + 7) // 8, 'big').decode()
    return message_décodé

def enregistrer(message):
    with open("message_décodé.txt", "w") as f:
        f.write(message)

#principal
message_codé="131311351425042412305024012545011210225555440342240014245242443323551122021213311233253501210115454153"
print(len(message_codé))
print(message_codé)
clé=int(input("Entrer le code"))
message_codé=message_codé[0:clé]
message=décoder(message_codé)
print(message)
enregistrer(message)