# parcinfo
Parc informatique d'un projet faite en django

# Information sur parcinfor

ParcInfo est projet que j ai realiser pour ma soutenance lorsque j'etais en stage 
ecole.
Cet projet consite a met en place un systeme de gestions des materiels (Ordinateur portable, impriment ect ..)

# Comment installé l'application parcinfo

1- Veuillez clone le projet sur votre marchine
   par exemple: 
   installé git sur votre machine
   
    git clone https/xxxxxxxxxxxxxx

2- Creer un environnement de travail sur votre marchine en local
   par exemple:
   
     virtualenv le non_de_dossier

3- Activez cette environnement en tapan cette commande:
   # systeme window
      xxxxxxxxxxxxxxxx
  # system linux
     soure nom_de_dossier/bin/activate
4- Entrez cette commande pour installé les packages neccessaire qui se trouve dans le fichier requirements.txt.
      Tapez cette commande: 
      
      pip install -m requirements.txt

5- Executer le serveur local du framework django
   Avec cette commande: python manage.py runserver
   Vous verez un lien copier cette dans votre navigateur.

    http://127.0.0.1:8080

6- La page vous demanderas de vous connecté.
   Pour créer un super-utilisateur tapez dans le console de votre projet  cette commande pour en creer un :

     python manage.py createsuperuser
