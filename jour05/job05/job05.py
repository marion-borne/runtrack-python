def chiffrement_cesar(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_chiffre = ''

    for lettre in message:
        if lettre in alphabet:  # On ne décale que les lettres de l'alphabet
            # On trouve la nouvelle position en prenant en compte le dépassement
            nouvelle_position = (alphabet.index(lettre) + decalage) % len(alphabet)
            message_chiffre += alphabet[nouvelle_position]
        else:
            message_chiffre += lettre  # On laisse les autres caractères inchangés

    return message_chiffre


# Exemple d'utilisation :
message = "Bonjour de César"
decalage = 3
print(chiffrement_cesar(message, decalage))  # Affiche "erqmrxu"