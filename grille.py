class Grille:
    """Ggrille sur laquelle sont positionnés les bateaux et les tirs"""

    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nombre_lignes = nombre_lignes
        self.nombre_colonnes = nombre_colonnes

    def afficher():
        print("  A B C D E F G H")
        for i, ligne in enumerate(Grille):
            print(f"{i+1} {' '.join(ligne)}")

    def tirer(x, y):
        Grille[x][y] = 'x'