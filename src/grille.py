import random


class Grille:
    """Ggrille sur laquelle sont positionnés les bateaux et les tirs"""

    def __init__(self, nombre_lignes, nombre_colonnes):
        self.matrice = [["~" for _ in range(nombre_colonnes)]
                        for _ in range(nombre_lignes)]
        self.nombre_colonnes = nombre_colonnes
        self.nombre_lignes = nombre_lignes

    def __str__(self):
        result = ("  " +
                  " ".join(chr(65 + i) for i in range(self.nombre_colonnes)) +
                  "\n")
        for i, ligne in enumerate(self.matrice):
            result += f"{i+1} {' '.join(ligne)}\n"
        return result

    def tirer(self, x, y, touche='x'):
        self.matrice[x-1][y-1] = touche

    def ajoute(self, bateau):
        pos = []
        try:
            for e in bateau.positions:
                if (e[0] < 0
                        or e[0] >= len(self.matrice)
                        or e[1] < 0
                        or e[1] >= len(self.matrice[0])):
                    raise ValueError("Position hors matrice")
            for e in bateau.positions:
                self.matrice[e[0]][e[1]] = "⛵"
                pos.append(self.matrice[e[0]][e[1]])
            return pos
        except Exception:
            pass

    def peut_placer(self, bateau):
        """Vérifie que toutes les cases du bateau
        sont dans la grille et libres."""
        for x, y in bateau.positions:
            if (x < 0
                    or x >= self.nombre_lignes
                    or y < 0
                    or y >= self.nombre_colonnes):
                return False
            if self.matrice[x][y] != "~":
                return False
        return True

    def placer_bateau_aleatoire(self, classe_bateau):
        """Calcule toutes les positions possibles puis choisit au hasard."""
        solutions = []
        for x in range(self.nombre_lignes):
            for y in range(self.nombre_colonnes):
                for horizontal in [True, False]:
                    b = classe_bateau(x, y, horizontal)  # création temporaire
                    if self.peut_placer(b):
                        solutions.append(b)
        choix = random.choice(solutions)
        self.ajoute(choix)

    def bateaux(self):
        """Trouve la position des bateaux"""
        positions = []
        for i in range(self.nombre_lignes):
            for j in range(self.nombre_colonnes):
                if self.matrice[i][j] != "~":
                    positions.append((i, j))
        return positions
