"""Nom : "Plouf dans l'eau"
Utilisateur : un joueur
Story : On veut pouvoir gérer les tirs de l'adversaire
Actions :
"""
from grille import Grille
grille = Grille(5,8)
nb_coups = 0
nb_max = 30

while nb_coups != nb_max:
    print(grille)

    coordonnees = input("Choisez une coordonnée pour le tir (chiffres séparés d'un espace)")
    
    try:
        if 0 < ord(coordonnees[0])-64 < 9 and  0 < (int(coordonnees[2])) < 6 :
            grille.tirer(int(coordonnees[2]), ord(coordonnees[0])-64 )
            nb_coups+=1
        else:
            print("Erreur : coordonnées non valides")
    except Exception as e:
        print("Erreur : Frappe invalide")