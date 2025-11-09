class Grille:
    """Ggrille sur laquelle sont positionnés les bateaux et les tirs"""
    matrice = []
    nombre_colonnes = 0

    def __init__(self, nombre_lignes, nombre_colonnes):
        self.matrice = [["~" for _ in range(nombre_colonnes)] for _ in range(nombre_lignes)]
        self.nombre_colonnes = nombre_colonnes
        self.nombre_lignes = nombre_lignes

    def __str__(self):
        result = "  " + " ".join(chr(65 + i) for i in range(self.nombre_colonnes)) + "\n"
        for i, ligne in enumerate(self.matrice):
            result += f"{i+1} {' '.join(ligne)}\n"
        return result

    def tirer(self, x, y):
        self.matrice[x-1][y-1] = 'x'