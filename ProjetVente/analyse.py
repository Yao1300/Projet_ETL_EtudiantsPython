def statistiques(df):
    """
    Calcul des statistiques et KPI.
    """

    chiffre_affaires = df["Chiffre_Affaires"].sum()
    quantite_totale = df["Quantite"].sum()
    prix_moyen = df["Prix_Unitaire"].mean()

    return {
        "Chiffre_Affaires_Total": chiffre_affaires,
        "Quantite_Totale": quantite_totale,
        "Prix_Moyen": prix_moyen
    }