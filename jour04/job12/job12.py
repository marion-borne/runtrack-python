ma_liste = [64, 74, 25, 50, 22, 11, 99]
def triB(liste):
    n = 0
    # Compter le nombre d'éléments dans la liste
    for _ in liste:
        n = n + 1

    # Tri à bulles
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

# Test du programme
print(triB(ma_liste))