# Projet_ISN
 
#Partie 1 : encoder / décoder texte
<h1> JAAJ <h1>

	- message_à_encoder.txt
		Desctiption : message texte
		Contenu : coordonnées GPS à dissimuler
	- Encoder.py
		Fichiers en entrée : message_à_encoder.txt
		Algo :
			Ouvrir fichier texte
			Copier contenu fichier dans variable "message"
			Convertir "message" en suite de chiffres
			Passer en base 6 pour gagner de l'espace
				Valeur max : 255 donc le dernier chiffre doit
