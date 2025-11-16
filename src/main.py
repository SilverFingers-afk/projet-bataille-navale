from grille import Grille
from bateau import PorteAvion
from bateau import Torpilleur
from bateau import Croiseur
from bateau import SousMarin

grille = Grille(8, 10)
g = Grille(8, 10)
porteavion = g.placer_bateau_aleatoire(PorteAvion)
torpilleur = g.placer_bateau_aleatoire(Torpilleur)
croiseur = g.placer_bateau_aleatoire(Croiseur)
sousmarin = g.placer_bateau_aleatoire(SousMarin)

nb_coups = 0
nb_max = 30
print(ord('A'))
while nb_coups != nb_max:
    print(g)
    print(grille)
    coordonnees = input("Choisez une coordonnée pour le tir "
                        "(chiffres séparés d'un espace)")
    try:
        if 0 < ord(coordonnees[0])-64 < 11 and 0 < (int(coordonnees[2])) < 9:
            if g.matrice[int(coordonnees[2])-1][ord(coordonnees[0])-65] == "⛵":
                grille.tirer(int(coordonnees[2]),
                             ord(coordonnees[0])-64,
                             "💣")
            else:
                grille.tirer(int(coordonnees[2]), ord(coordonnees[0])-64)
            nb_coups += 1
        else:
            print("Erreur : coordonnées non valides")
    except Exception as e:
        print(e)
print("Nombre de coups : " + nb_coups)
