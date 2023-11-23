ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]


# Définition de la fonction qui supprime les doublons
def list():
    liste_sans_doublons = []

    # Parcours de chaque élément de la liste initiale
    for i in ma_liste:
        if i not in liste_sans_doublons:
            liste_sans_doublons.append(i)

    return liste_sans_doublons


print(list())