from grille import Grille
from bateau import PorteAvion
from bateau import Torpilleur
from bateau import Croiseur
from bateau import SousMarin

grille = Grille(8, 10)
grille.placer_bateau_aleatoire(PorteAvion)
grille.placer_bateau_aleatoire(Torpilleur)
grille.placer_bateau_aleatoire(Croiseur)
grille.placer_bateau_aleatoire(SousMarin)
nb_coups = 0
nb_max = 30

while nb_coups != nb_max:
    print(grille)

    coordonnees = input("Choisez une coordonnée pour le tir "
                        "(chiffres séparés d'un espace)")

    try:
        if 0 < ord(coordonnees[0])-64 < 9 and 0 < (int(coordonnees[2])) < 6:
            grille.tirer(int(coordonnees[2]), ord(coordonnees[0])-64)
            nb_coups += 1
        else:
            print("Erreur : coordonnées non valides")
    except Exception:
        print("Erreur : Frappe invalide")
print("Nombre de coups : " + nb_coups)
