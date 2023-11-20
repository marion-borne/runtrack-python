montant_initial = float(input("Veuillez saisir le montant initial de l'investissement : "))

taux_rendement_annuel = float(input("Veuillez saisir le taux de rendement annuel en pourcentage : "))

periode_simulation = int(input("Veuillez saisir la période de simulation en années : "))

capital_augmente = 5000
montant_initial += capital_augmente

taux_rendement_annuel_augmente = taux_rendement_annuel + 2

montant_final_apres_augmentation = montant_initial * (1 + taux_rendement_annuel_augmente / 100) ** periode_simulation

montant_initial_apres_retrait = montant_final_apres_augmentation * 0.9

taux_rendement_annuel_diminue = taux_rendement_annuel_augmente - 1

montant_final_apres_retrait = montant_initial_apres_retrait * (1 + taux_rendement_annuel_diminue / 100) ** periode_simulation

print("\nRésultats de la simulation après retrait et diminution du rendement :")
print(f"Montant initial de l'investissement : {montant_initial} euros")
print(f"Taux de rendement annuel augmenté : {taux_rendement_annuel_augmente}%")
print(f"Montant final de l'investissement après augmentation : {montant_final_apres_augmentation:.2f} euros")
print(f"Montant initial après retrait de 10% : {montant_initial_apres_retrait:.2f} euros")
print(f"Taux de rendement annuel diminué : {taux_rendement_annuel_diminue}%")
print(f"Montant final de l'investissement après retrait et diminution du rendement : {montant_final_apres_retrait:.2f} euros")