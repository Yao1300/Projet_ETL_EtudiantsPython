import pandas as pd
import numpy as np


def statistiques_generales(df):
    """
    Analyse descriptive des données
    """

    resultats = {
        "nombre_lignes": len(df),
        "moyenne": df["montant"].mean(),
        "maximum": df["montant"].max(),
        "minimum": df["montant"].min(),
        "ecart_type": df["montant"].std()
    }

    return resultats


def analyse_clients(df):
    """
    Analyse du comportement client
    """

    analyse = df.groupby("client_id").agg(
        total_achats=("montant", "sum"),
        nombre_commandes=("id_commande", "count"),
        moyenne_panier=("montant", "mean")
    )

    return analyse


def segmentation_rfm(df):
    """
    Analyse RFM :
    Recency - Frequency - Monetary
    """

    rfm = df.groupby("client_id").agg(
        recence=("date", "max"),
        frequence=("id_commande", "count"),
        valeur=("montant", "sum")
    )

    return rfm