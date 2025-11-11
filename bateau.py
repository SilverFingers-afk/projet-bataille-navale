class Bateau:
  """Classe représentant un bateau dans le jeu."""

  def __init__(self, ligne, colonne, longueur = 1, vertical = False):
    self.ligne = ligne
    self.colonne = colonne
    self.longueur = longueur
    self.vertical = vertical

  @property
  def positions(self):
    if self.vertical == False:
      return [(self.ligne, i) for i in range(self.colonne, self.colonne + self.longueur)]
    else:
      return [(i, self.colonne) for i in range(self.ligne, self.ligne + self.longueur)]