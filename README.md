# Projet_ISN
 
Partie 1 : encoder / décoder texte
<blockquote> Dossier : Encodage texte </blockquote>  
=
message_à_encoder.txt
-
Desctiption : message texte  
Contenu : coordonnées GPS à dissimuler  

Encoder.py
-
<blockquote> Fichiers en entrée : message_à_encoder.txt </blockquote>  
<strong> Algo : </strong>
</br> Ouvrir fichier texte
</br> Copier contenu fichier dans variable "message"
</br> Convertir "message" en suite de chiffres
</br> Passer en base 6 pour gagner de l'espace
</br> <em> REM : Valeur max : 255 donc le dernier chiffre ne doit pas dépasser 5 d'où la base 6 </em>
</br> Enregistrer le message ainsi encodé dans une variable : message_codé

Decoder.py
-
<blockquote> Fichiers en sortie : message_décodé.txt </blockquote>  
<strong> Algo : </strong>
</br> Passer en base 10 le message codé
</br> Convertir le message codé en caractères
</br> Enregistrer le message décodé dans un fichier : message_décodé
