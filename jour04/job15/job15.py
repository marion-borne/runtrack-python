liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]


def listeA():
    # Créer une nouvelle liste pour stocker les nombres arrondis
    liste_arrondie = []

    # Parcourir chaque nombre dans la liste
    for i in range(len(liste)):
        # Arrondir le nombre et l'ajouter à la nouvelle liste
        liste_arrondie.append(int(liste[i]) if liste[i] - int(liste[i]) < 0.5 else int(liste[i]) + 1)

    # Trier la liste arrondie
    for i in range(len(liste_arrondie)):
        for j in range(i + 1, len(liste_arrondie)):
            if liste_arrondie[i] > liste_arrondie[j]:
                # Échanger les nombres
                liste_arrondie[i], liste_arrondie[j] = liste_arrondie[j], liste_arrondie[i]

    return liste_arrondie


print(listeA())