nom = "Tshirt"

prix= 50

stock = 100

print(f"""Article : {nom}
    prix : {prix}
    stock : {stock}""")

saisie = int(input("Entrez la quantité que vous souhaitez acheter : "))

print (f"""Article : {nom}
    prix : {prix*1.1}
    stock : {stock-saisie}""")