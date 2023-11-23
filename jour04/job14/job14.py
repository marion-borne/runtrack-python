# On définit une liste avec un entier et une chaîne de caractères
liste = [5, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"]

# On définit la fonction 'my_long_word' qui prend une liste en argument
def my_long_word(liste):
    # On extrait l'entier et la chaîne de caractères de la liste
    n = liste[0]
    text = liste[1]
    # On divise la chaîne de caractères en mots
    words = text.split(' ')
    # On crée une liste vide pour stocker les mots longs
    long_words = []
    # On parcourt chaque mot de la liste de mots
    for word in words:
        # On initialise un compteur à zéro pour chaque mot
        count = 0
        # On parcourt chaque lettre du mot
        for letter in word:
            # On incrémente le compteur pour chaque lettre
            count = count + 1
        # Si le nombre de lettres dans le mot est supérieur à n, on ajoute le mot à la liste des mots longs
        if count > n:
            long_words.append(word)
    return ' '.join(long_words)


print(my_long_word(liste))