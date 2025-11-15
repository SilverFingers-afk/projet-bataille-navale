"""Nom : "chevauchement"
Utilisateur : un joueur
Story : Positionner des bateaux sans chevauchement
"""
from grille import Grille
from bateau import Bateau
from bateau import PorteAvion
from bateau import Torpilleur
from bateau import Croiseur
from bateau import SousMarin


def chevauchement(bat1, bat2):
    for e1 in bat1.positions:
        for e2 in bat2.positions:
            if e1 == e2:
                return False
    return True


porteavion = PorteAvion(2, 2, False)
torpilleur = Torpilleur(3, 5, False)
croiseur = Croiseur(4, 1, False)
sousmarin = SousMarin(0, 0, True)
b2 = Bateau(2, 3, 3, False)
b3 = Bateau(1, 0, longueur=3, vertical=False)
grille = Grille(8, 10)

grille.ajoute(porteavion)
grille.ajoute(torpilleur)
grille.ajoute(croiseur)
grille.ajoute(sousmarin)
print(sousmarin.positions)
print(grille)
print(b3.coulé(grille))
for e in b3.positions:
    grille.tirer(e[0]+1, e[1]+1)
print(b3.coulé(grille))
print(grille)
