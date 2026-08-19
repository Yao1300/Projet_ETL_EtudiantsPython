import pandas as pd


def transform_data(df):

    print("\n===== TRANSFORMATION =====")

    # Nettoyage des noms de colonnes
    df.columns = df.columns.str.strip().str.lower()

    df = df.drop_duplicates()

    # Conversion de la date
    df["date"] = pd.to_datetime(df["date"])

    # Suppression des lignes vides
    df = df.dropna()

    # Calcul du chiffre d'affaires
    df["chiffre_affaires"] = (
        df["quantite"] * df["prix_unitaire"]
    )

    # Noms pour SQL Server
    df = df.rename(columns={
        "date": "DateVente",
        "client": "Client",
        "ville": "Ville",
        "produit": "Produit",
        "categorie": "Categorie",
        "quantite": "Quantite",
        "prix_unitaire": "Prix_Unitaire",
        "chiffre_affaires": "Chiffre_Affaires"
    })

    print("Transformation réussie")
    print("Nombre de lignes :", len(df))
    print("Colonnes finales :", df.columns.tolist())

    return df