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
bateaux = [porteavion, torpilleur, croiseur, sousmarin]
nb_coups = 0
nb_max = 30
victory = False

while nb_coups != nb_max:
    print(grille)
    coordonnees = input("Choisez une coordonnée pour le tir "
                        "(Lettre majuscule puis chiffres séparés d'un espace)")
    try:
        if 0 < ord(coordonnees[0])-64 < 11 and 0 < (int(coordonnees[2])) < 9:
            if g.matrice[int(coordonnees[2])-1][ord(coordonnees[0])-65] == "⛵":
                grille.tirer(int(coordonnees[2]),
                             ord(coordonnees[0])-64,
                             "💣")
                nouvelle_liste = []
                for b in bateaux:
                    if b.coule(grille):
                        print(b.nom + " coulé")
                        grille.ajoute(b, b.icone)
                    else:
                        nouvelle_liste.append(b)
                bateaux = nouvelle_liste
            else:
                grille.tirer(int(coordonnees[2]), ord(coordonnees[0])-64)
            nb_coups += 1
            if bateaux == []:
                victory = True
                break
        else:
            print("Erreur : coordonnées non valides")
    except Exception as e:
        print(e)

if victory:
    print("Partie gagnée!")
else:
    print("Partie perdue!")
print("Nombre de coups : " + str(nb_coups))
print(grille)
print(g)
