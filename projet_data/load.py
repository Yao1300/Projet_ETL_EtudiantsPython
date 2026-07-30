import pandas as pd
from sqlalchemy import create_engine


def load_csv(df, fichier):
    """
    Chargement des données dans un fichier CSV
    """

    df.to_csv(
        fichier,
        index=False
    )

    print("Données exportées avec succès")


def load_database(df):
    """
    Chargement des données dans une base SQL
    """

    # Connexion à la base de données
    engine = create_engine(
        "mysql+pymysql://user:password@localhost/database"
    )

    # Insertion des données dans une table
    df.to_sql(
        "clients",
        con=engine,
        if_exists="append",
        index=False
    )

    print("Données chargées dans la base")


def load_excel(df, fichier):
    """
    Export des données vers Excel
    """

    df.to_excel(
        fichier,
        index=False
    )