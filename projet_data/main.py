# ============================================================
# Fichier : main.py
# Projet : Analyse ETL des performances des étudiants
#
# Rôle :
# Ce fichier orchestre l'ensemble du pipeline ETL.
# ============================================================


# ============================================================
# Importation des fonctions nécessaires
# ============================================================

from extract import (
    extraire_etudiants,
    extraire_notes,
    extraire_presence
)

from transform import (
    clean_data,
    transform_data
)

from analyse import statistiques_generales
from graphique import graphique_ventes
from load import load_database


# ============================================================
# Fonction principale du pipeline ETL
# ============================================================

def main():
    """
    Fonction principale du pipeline ETL.
    """

    # ========================================================
    # 1. EXTRACTION
    # ========================================================

    print("\n===== ÉTAPE 1 : EXTRACTION =====")

    etudiants = extraire_etudiants()
    notes = extraire_notes()
    presence = extraire_presence()
    
    print("\n===== COLONNES ÉTUDIANTS =====")
    print(etudiants.columns.tolist())

    print("\n===== COLONNES NOTES =====")
    print(notes.columns.tolist())

    print("\n===== COLONNES PRÉSENCE =====")
    print(presence.columns.tolist())

    print("\n--- Étudiants ---")
    print(etudiants.head())

    print("\n--- Notes ---")
    print(notes.head())

    print("\n--- Présence ---")
    print(presence.head())


    # ========================================================
    # 2. NETTOYAGE ET TRANSFORMATION
    # ========================================================

    print("\n===== ÉTAPE 2 : TRANSFORMATION =====")

    etudiants = clean_data(etudiants)
    etudiants = transform_data(etudiants)


    # ========================================================
    # 3. ANALYSE
    # ========================================================

    print("\n===== ÉTAPE 3 : ANALYSE =====")

    resultats = statistiques_generales(etudiants)

    print("\n--- Résultats ---")
    print(resultats)


    # ========================================================
    # 4. VISUALISATION
    # ========================================================

    print("\n===== ÉTAPE 4 : VISUALISATION =====")

    graphique_ventes(etudiants)


    # ========================================================
    # 5. CHARGEMENT
    # ========================================================

    print("\n===== ÉTAPE 5 : CHARGEMENT =====")

    load_database(etudiants)


    # ========================================================
    # FIN DU PIPELINE
    # ========================================================

    print("\n===== PIPELINE ETL TERMINÉ =====")


# ============================================================
# Point d'entrée du programme
# ============================================================

if __name__ == "__main__":
    main()