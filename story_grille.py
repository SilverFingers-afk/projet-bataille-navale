"""Nom : "Plouf dans l'eau"
Utilisateur : un joueur
Story : On veut pouvoir gérer les tirs de l'adversaire
Actions :
"""

"""créer une grille à 5 lignes et 8 colonnes"""
nb_coups = 0
nb_max = 30

while nb_coups != nb_max:
    print(grille(5))

    coordonnees = input("Choisez une coordonnée pour le tir (chiffres séparés d'un espace)")

    if True:
        """Tire à l'endroit et change d'icône selon raté ou touché"""
    else:
        """message d'erreur: coordonnées incorrectes, on reboucle sans compte le coup"""