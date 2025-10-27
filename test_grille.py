from grille import Grille

def test_init():
  """Teste que l'on peut créer un objet de la classe Grille."""
  try:
    grille = Grille(5,8)  # On essaie de créer un objet Grille
    print("Test réussi : un objet Grille a été créé avec succès.")
    grille.tirer(3, 3)
    grille.afficher()
  except Exception as e:
    print(f"Test échoué : {e}")

if __name__ == "__main__":
  test_init()