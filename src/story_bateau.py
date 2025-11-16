"""Nom : "chevauchement"
Utilisateur : un joueur
Story : Positionner des bateaux sans chevauchement
Actions :
créer un bateau b1
créer un bateau b2
Vérifier si les deux bateaux se chevauchent"""

from bateau import Bateau


def chevauchent(b1, b2):
    """Retourne True si au moins une position est commune."""
    return any(pos in b2.positions for pos in b1.positions)


print("=== User Story : Chevauchement ===")

# --- Cas 1 : bateaux qui se chevauchent ---
b1 = Bateau(0, 0, 3, True)
b2 = Bateau(0, 1, 3, True)

print("\nCas 1 : chevauchement attendu")
print("B1 :", b1.positions)
print("B2 :", b2.positions)
print("Chevauchent ?", chevauchent(b1, b2))

# --- Cas 2 : bateaux qui ne se chevauchent pas ---
b3 = Bateau(5, 5, 3, True)
b4 = Bateau(7, 5, 3, True)

print("\nCas 2 : pas de chevauchement attendu")
print("B3 :", b3.positions)
print("B4 :", b4.positions)
print("Chevauchent ?", chevauchent(b3, b4))
