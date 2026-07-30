import pandas as pd
import numpy as np


def clean_data(df):
    """
    Nettoyage des données
    """
    # Suppression des doublons
    df = df.drop_duplicates()

    # Gestion des valeurs manquantes
    df = df.fillna(0)

    return df


def transform_data(df):
    """
    Transformation des données
    """

    # Conversion d'une colonne en majuscule
    df["nom"] = df["nom"].str.upper()

    # Création d'une nouvelle variable
    df["total"] = df["prix"] * df["quantite"]

    # Normalisation d'une colonne numérique
    df["score"] = (
        df["score"] - df["score"].mean()
    ) / df["score"].std()

    return df