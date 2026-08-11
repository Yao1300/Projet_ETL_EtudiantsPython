# ============================================================
# Fichier : analyse.py
# Projet : Analyse ETL des performances des étudiants
#
# Rôle :
# Cette partie réalise l'analyse des données transformées.
# ============================================================


import pandas as pd
import numpy as np


# ============================================================
# Statistiques générales
# ============================================================

def statistiques_generales(df):
    """
    Analyse descriptive générale des données.
    """

    resultats = {
        "nombre_lignes": len(df),
        "nombre_colonnes": len(df.columns)
    }

    # --------------------------------------------------------
    # Sélection des colonnes numériques
    # --------------------------------------------------------

    colonnes_numeriques = df.select_dtypes(
        include=np.number
    ).columns

    # --------------------------------------------------------
    # Calcul des statistiques
    # --------------------------------------------------------

    for colonne in colonnes_numeriques:

        resultats[f"{colonne}_moyenne"] = df[colonne].mean()

        resultats[f"{colonne}_maximum"] = df[colonne].max()

        resultats[f"{colonne}_minimum"] = df[colonne].min()

        resultats[f"{colonne}_ecart_type"] = df[colonne].std()

    return resultats


# ============================================================
# Analyse des étudiants
# ============================================================

def analyse_etudiants(df):
    """
    Analyse générale des données des étudiants.
    """

    analyse = {
        "nombre_etudiants": len(df),
        "nombre_colonnes": len(df.columns)
    }

    return analyse


# ============================================================
# Analyse des notes
# ============================================================

def analyse_notes(df, colonne_note):
    """
    Analyse statistique des notes des étudiants.
    """

    resultats = {
        "nombre_notes": len(df),
        "moyenne": df[colonne_note].mean(),
        "note_maximale": df[colonne_note].max(),
        "note_minimale": df[colonne_note].min(),
        "ecart_type": df[colonne_note].std()
    }

    return resultats


# ============================================================
# Analyse des présences
# ============================================================

def analyse_presence(df, colonne_presence):
    """
    Analyse des données de présence des étudiants.
    """

    resultats = {
        "nombre_enregistrements": len(df),
        "nombre_presents": (
            df[colonne_presence] == 1
        ).sum(),
        "nombre_absents": (
            df[colonne_presence] == 0
        ).sum()
    }

    return resultats