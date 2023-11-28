def distance_parcourue(nombre_marches, hauteur_marche):
    # Convertir la hauteur de chaque marche en mètres
    hauteur_marche_m = hauteur_marche / 100

    # Calculer la hauteur totale du phare en mètres
    hauteur_phare_m = nombre_marches * hauteur_marche_m

    # Calculer la distance parcourue pour un aller-retour aux toilettes
    distance_aller_retour_m = 2 * hauteur_phare_m

    # Calculer la distance parcourue par jour (5 fois aux toilettes)
    distance_par_jour_m = 5 * distance_aller_retour_m

    # Calculer la distance parcourue par semaine (7 jours)
    distance_par_semaine_m = 7 * distance_par_jour_m

    return distance_par_semaine_m

# Exemple d'utilisation :
nombre_marches = 400
hauteur_marche = 15  # en cm
distance = distance_parcourue(nombre_marches, hauteur_marche)
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance:.2f} m par semaine.")