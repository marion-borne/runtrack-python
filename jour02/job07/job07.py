chaine = "abcdefghijklmnopqrstuvwxyz" * 10
longueur = len(chaine) 

for i in range(1, longueur * 2,2):
    if i <= longueur:
        print(chaine[:i])