import pandas as pd


def extract_data(fichier):

    df = pd.read_csv(
        fichier,
        encoding="utf-8"
    )

    print("Extraction réussie")
    print("Nombre de lignes :", len(df))
    print("Colonnes :", df.columns.tolist())

    return df