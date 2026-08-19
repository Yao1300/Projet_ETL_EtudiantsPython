from sqlalchemy import create_engine


def load_data(df):
    """
    Chargement des données dans SQL Server.
    """

    serveur = "localhost"
    base = "ETL_BI"

    connection_string = (
        "mssql+pyodbc://@"
        + serveur
        + "/"
        + base
        + "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )

    engine = create_engine(connection_string)

    df.to_sql(
        "Ventes",
        engine,
        if_exists="append",
        index=False
    )

    print("Données chargées dans SQL Server")