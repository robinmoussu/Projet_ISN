# Projet_ISN
 
Partie 1 : encoder / décoder texte
=
message_à_encoder.txt
-
Desctiption : message texte  
Contenu : coordonnées GPS à dissimuler  

Encoder.py
-
<blockquote> Fichiers en entrée : message_à_encoder.txt </blockquote>  
<strong> Algo : </strong>  
Ouvrir fichier texte  
Copier contenu fichier dans variable "message"  
Convertir "message" en suite de chiffres  
Passer en base 6 pour gagner de l'espace  
<em> Valeur max : 255 donc le dernier chiffre ne doit pas dépasser 5 d'où la base 6 <em>  
Enregistrer le message ainsi encodé dans une variable : message_codé