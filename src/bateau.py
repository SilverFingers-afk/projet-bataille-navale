class Bateau:
    """Classe représentant un bateau dans le jeu."""

    def __init__(self, ligne, colonne, nom, icone, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.nom = nom
        self.icone = icone
        self.longueur = longueur
        self.vertical = vertical

    @property
    def positions(self):
        """Retourne les positions de chaque point du bateau sur la grille"""
        if not self.vertical:
            return [(self.ligne, i) for i in range(self.colonne,
                                                   self.colonne + self.longueur)]
        else:
            return [(i, self.colonne) for i in range(self.ligne,
                                                     self.ligne + self.longueur)]

    def coule(self, grille):
        """Vérifie si tous les éléments du bateau
        sélectionnés sont coulés sur la grille"""
        for e in self.positions:
            if grille.matrice[e[0]][e[1]] != "💣":
                return False
        return True


class PorteAvion(Bateau):
    def __init__(self, x, y, vertical=False):
        super().__init__(x, y, "Porte-avion", "🚢", 4, vertical)


class Croiseur(Bateau):
    def __init__(self, x, y, vertical=False):
        super().__init__(x, y, "Croiseur", "⛴", 3, vertical)


class Torpilleur(Bateau):
    def __init__(self, x, y, vertical=False):
        super().__init__(x, y, "Torpilleur", "🚣", 2, vertical)


class SousMarin(Bateau):
    def __init__(self, x, y, vertical=False):
        super().__init__(x, y, "Sous-marin", "🐟", 2, vertical)
