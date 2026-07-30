import matplotlib.pyplot as plt
import pandas as pd


def graphique_ventes(df):
    """
    Affiche l'évolution des ventes dans le temps
    """

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["date"],
        df["montant"]
    )

    plt.title("Évolution des ventes")
    plt.xlabel("Date")
    plt.ylabel("Montant")

    plt.xticks(rotation=45)

    plt.show()


def graphique_clients(df):
    """
    Affiche la répartition des clients
    """

    repartition = df.groupby("categorie")["client_id"].count()

    repartition.plot(
        kind="bar",
        figsize=(8, 4)
    )

    plt.title("Répartition des clients")
    plt.xlabel("Catégorie")
    plt.ylabel("Nombre de clients")

    plt.show()