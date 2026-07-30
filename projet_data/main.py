# Importation des fonctions nécessaires
from extract import extract_data
from transform import clean_data, transform_data
from analyse import statistiques_generales
from graphique import graphique_ventes
from load import load_database


def main():
    """
    Fonction principale du pipeline ETL
    """

    # 1. Extraction des données
    data = extract_data()

    # 2. Nettoyage et transformation
    data = clean_data(data)
    data = transform_data(data)

    # 3. Analyse des données
    resultats = statistiques_generales(data)

    print(resultats)

    # 4. Visualisation
    graphique_ventes(data)

    # 5. Chargement des données finales
    load_database(data)


# Point d'entrée du programme
if __name__ == "__main__":
    main()