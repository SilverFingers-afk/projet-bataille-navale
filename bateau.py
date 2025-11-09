class Bateau:
  """Classe représentant un bateau dans le jeu."""

  def __init__(self, ligne, colonne, longueur = 1, est_vertical = False):
    self.ligne = ligne
    self.colonne = colonne
    self.longueur = longueur
    self.est_vertical = est_vertical

  @property
  def positions(self):
    if self.est_vertical == False:
      return [(self.ligne, i) for i in range(self.colonne, self.colonne + self.longueur)]
    else:
      return [(i, self.colonne) for i in range(self.ligne, self.ligne + self.longueur)]