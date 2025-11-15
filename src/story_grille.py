"""Nom : "Plouf dans l'eau"
Utilisateur : un joueur
Story : On veut pouvoir gérer les tirs de l'adversaire
Actions :
créer une grille à 5 lignes et 8 colonnes
afficher la grille à l'écran
demande à l'utilisateur de rentrer deux coordonnées x et y
tier à l'endroit indiqué sur la grille
retour en 2"""

from grille import Grille

print("=== User Story : Plouf dans l'eau ===")
grille = Grille(5, 8)  # Création de la grille
while True:  # Retour en 2
    print(grille)

    coordonnees = input("Choisez une coordonnée pour le tir")

    if True:
        """Tire à l'endroit et change d'icône selon raté ou touché"""
    else:
        """message d'erreur: coordonnées incorrectes, on
        reboucle sans compte le coup"""
