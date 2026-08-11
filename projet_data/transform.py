# ============================================================
# Fichier : transform.py
# Projet : Analyse ETL des performances des étudiants
#
# Rôle :
# Nettoyage et transformation des données extraites.
# ============================================================

import pandas as pd
import numpy as np


# ============================================================
# Nettoyage des données
# ============================================================

def clean_data(df):
    """
    Nettoie les données.

    - Suppression des doublons
    - Gestion des valeurs manquantes
    """

    # --------------------------------------------------------
    # Suppression des doublons
    # --------------------------------------------------------

    df = df.drop_duplicates()

    # --------------------------------------------------------
    # Gestion des valeurs manquantes
    # --------------------------------------------------------

    df = df.fillna(0)

    return df


# ============================================================
# Transformation des données
# ============================================================

def transform_data(df):
    """
    Transforme les données.
    """

    # Affichage des colonnes disponibles
    print("\n===== COLONNES DISPONIBLES =====")
    print(df.columns.tolist())

    return df