# Projet_ISN
 
Partie 1 : encoder / décoder texte
=
<blockquote> Dossier : Encodage texte </blockquote>  

message_à_encoder.txt
-
Desctiption : message texte  
Contenu : coordonnées GPS à dissimuler  

message_décodé.txt
-
Desctiption : message texte  
Contenu : message décodé par le programme

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

Partie 2 : encoder image
=
<blockquote> Dossier : Encodage image </blockquote>  

image.bmp
-
Type : image bmp  
Taille : 800x600px  
Description	: Delonix regia at the bank of Brisbane River in South Brisbane, Queensland, Australia  
Auteur : Kgbo  
Source : <https://commons.wikimedia.org/wiki/File:Delonix_regia_at_the_bank_of_Brisbane_River_in_South_Brisbane,_Queensland,_Australia.jpg>  
License : Creative Commons Attribution-Share Alike 4.0 International  

Image.py
-
<blockquote> Fichiers en entrée : image.bmp, message_à_encoder.txt </blockquote>  
<blockquote> Fichiers en sortie : image_sortie.bmp </blockquote>  
<strong> Algo : </strong>
</br> Ouvrir l'image
</br> Vérifier si le message codé rentrera sur l'image
</br> Si il est trop long, afficher un message d'erreur
</br> Sinon, faire en sorte que la longueur du message codé soit la même que la capacité de l'image en ajoutant des 0
</br> Créer une matrice par couleur
</br> Dans chaque matrice, remplacer le bit de poids faible de chaque pixel par le bit d'indice "compteur" du message codé
</br> À chaque passage, ajouter 1 au compteur
</br> Créer une matrice de sortie
</br> Remplacer les valeurs cette matrice par les valeurs des 3 matrices de couleur
</br> Enregistrer cette matrice dans le fichier image_sortie