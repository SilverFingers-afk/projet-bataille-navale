"""Nom : "chevauchement"
Utilisateur : un joueur
Story : Positionner des bateaux sans chevauchement
"""

from grille import Grille
from bateau import Bateau
b1 = Bateau(2, 2, 3, True)
b2 = Bateau(2, 3, 3, False)
b3 = Bateau(1, 0, longueur=3, vertical=False)
grille = Grille(2,3)
def chevauchement(bat1, bat2):
  for e1 in bat1.positions:
    for e2 in bat2.positions:
      if e1 == e2:
        return False
  return True

grille.ajoute(b3)
print(grille)
print(b3.coulé(grille))
for e in b3.positions:
  grille.tirer(e[0]+1, e[1]+1)
print(b3.coulé(grille))
print(grille)