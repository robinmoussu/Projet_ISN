# Projet_ISN
 
Partie 0 : fonctionnement
=
Encodage
-
<p> Pour cacher un texte dans une image, utiliser le dossier "Encodage image", avec une image nomée "image.bmp", le message dans le fichier "message_à_encoder.txt" et
lancer le programme "Encodage_image.py". Il en ressort le fichier "image_sortie.bmp" identique à la première visuellement mais contenant le message codé </p>

Décodage
-
<p> Pour extraire un message d'une image, utiliser le dossier "Décodage image", avec une image (crée avec le premier dossier) "image_sortie.bmp" et lancer le programme
"Décodage_image.py". Il en ressort le fichier "message_décodé.txt" contenant le message secret </p>

Partie 1 : encoder image
=
<blockquote> Dossier : Encodage image </blockquote>  

Algo d'encodage
-
</br> Ouvrir fichier texte "message_à_encoder.txt"
</br> Copier contenu fichier dans variable "message"
</br> Convertir "message" en suite de chiffres binaires puis en base 10
</br> Passer en base 6 pour gagner de l'espace
</br> <em> REM : Valeur max : 255 donc le dernier chiffre ne doit pas dépasser 5 d'où la base 6 </em>
</br> Enregistrer le message ainsi encodé dans une variable : "message_codé"

Fichiers
-
Message_à_encoder.txt
-
Desctiption : message texte  
Contenu : coordonnées GPS à dissimuler pour l'exemple

image.bmp
-
Type : image bmp  
Taille : 800x600px  
Description	: Delonix regia at the bank of Brisbane River in South Brisbane, Queensland, Australia  
Auteur : Kgbo  
Source : <https://commons.wikimedia.org/wiki/File:Delonix_regia_at_the_bank_of_Brisbane_River_in_South_Brisbane,_Queensland,_Australia.jpg>  
License : Creative Commons Attribution-Share Alike 4.0 International  

image_sortie.bmp
-
Desctiption : image délivrée par le programme contenant le message secret

Encodage_image.py
-
<blockquote> Fichiers en entrée : image.bmp, message_à_encoder.txt </blockquote>  
<blockquote> Fichiers en sortie : image_sortie.bmp </blockquote>  
<strong> Algo : </strong>
</br> - Ouvrir l'image "image.bmp" dans "im1"
</br> - Ouvrir le fichier texte et l'encoder (voir algo)
</br> - Afficher la clé qui permettra de le décoder, qui correspond à la longueur de "message_codé"
</br> - Vérifier si le message codé rentrera sur l'image
</br> - Si il est trop long, afficher un message d'erreur
</br> - Sinon, faire en sorte que la longueur du message codé soit la même que la capacité de l'image en ajoutant des 0, pour éviter les dépassements
</br> - Créer une matrice par couleur
</br> - Dans chaque matrice, remplacer le bit de poids faible de chaque couleur de chaque pixel par le bit d'indice "compteur" du message codé
</br> - À chaque passage, ajouter 1 au compteur
</br> - Créer une image de sortie "im2"
</br> - Remplacer les valeurs cette image par les valeurs des 3 matrices de couleur
</br> - Enregistrer cette image dans le fichier "image_sortie.bmp"

Partie 2 : décoder image
=

<blockquote> Dossier : Décodage image </blockquote>  

Algo de décodage
-
</br> Passer en base 10 le message codé
</br> Convertir le message codé en caractères
</br> Enregistrer le message décodé dans un fichier : "message_décodé.txt"

message_décodé.txt
-
Desctiption : message texte  
Contenu : message décodé par le programme

image_sortie.bmp
-
Desctiption : image délivrée par le programme d'encodage contenant le message secret

Décodage_image.py
-
<blockquote> Fichiers en sortie : message_décodé.txt </blockquote>  
<strong> Algo : </strong>
</br> - Ouvrir l'image "image_sortie.bmp" du premier programme
</br> - Récuprérer le message en copiant le bit de poids faible de chaque couleur de chaque pixel
</br> - Ne garder que le message en tronquant tous les 0, à l'aide de la valeur de la "clé"
</br> - Afficher "message_codé" ainsi récupéré
</br> - Décoder "message_codé"