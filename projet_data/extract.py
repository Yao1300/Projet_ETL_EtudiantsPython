# ============================================================
# Fichier : extract.py
# Projet : Analyse ETL des performances des étudiants
#
# Rôle :
#   Cette partie réalise l'étape E (Extract) du pipeline ETL.
#
#   Elle permet :
#       - de lire les fichiers CSV
#       - de contrôler l'existence des fichiers
#       - de gérer les erreurs de lecture
#       - de retourner des DataFrames pandas
#
# Bibliothèques utilisées :
#       pandas : manipulation des données
#       os     : gestion des chemins fichiers
#       logging: suivi des opérations
#
# ============================================================


import pandas as pd
import os
import logging



# ============================================================
# Configuration du système de journalisation
# ============================================================

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)



# ============================================================
# Fonction générique de lecture CSV
# ============================================================

def lire_csv(chemin_fichier):

    """
    Cette fonction lit un fichier CSV et retourne
    un DataFrame pandas.

    Paramètre :
        chemin_fichier : chemin complet du fichier CSV

    Retour :
        DataFrame pandas
    """


    try:

        # ----------------------------------------------------
        # Vérification de l'existence du fichier
        # ----------------------------------------------------

        if not os.path.exists(chemin_fichier):

            raise FileNotFoundError(

                f"Le fichier {chemin_fichier} n'existe pas"

            )



        # ----------------------------------------------------
        # Lecture du fichier CSV avec pandas
        # ----------------------------------------------------

        df = pd.read_csv(

            chemin_fichier,

            encoding="utf-8"

        )



        logging.info(

            f"Extraction réussie : {chemin_fichier}"

        )


        logging.info(

            f"Nombre de lignes extraites : {len(df)}"

        )



        return df



    except FileNotFoundError as erreur:


        logging.error(erreur)


        raise



    except Exception as erreur:


        logging.error(

            f"Erreur pendant la lecture du fichier : {erreur}"

        )


        raise





# ============================================================
# Extraction des étudiants
# ============================================================

def extraire_etudiants():

    """
    Charge le fichier Etudiants.csv
    """


    chemin = (

        "../data/Etudiants.csv"

    )


    return lire_csv(chemin)





# ============================================================
# Extraction des notes
# ============================================================

def extraire_notes():

    """
    Charge le fichier Notes.csv
    """


    chemin = (

        "../data/Notes.csv"

    )


    return lire_csv(chemin)





# ============================================================
# Extraction des présences
# ============================================================

def extraire_presence():

    """
    Charge le fichier Presence.csv
    """


    chemin = (

        "../data/Presence.csv"

    )


    return lire_csv(chemin)





# ============================================================
# Test du module seul
# ============================================================

if __name__ == "__main__":


    print("\n===== TEST EXTRACTION =====\n")



    etudiants = extraire_etudiants()


    notes = extraire_notes()


    presence = extraire_presence()



    print("\n--- Etudiants ---")

    print(etudiants.head())



    print("\n--- Notes ---")

    print(notes.head())



    print("\n--- Présence ---")

    print(presence.head())

