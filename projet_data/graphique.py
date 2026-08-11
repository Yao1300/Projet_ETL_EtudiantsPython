# ============================================================
# Fichier : graphique.py
# Projet : Analyse ETL des performances des étudiants
#
# Rôle :
# Cette partie réalise la visualisation des données.
# ============================================================


import matplotlib.pyplot as plt
import pandas as pd


# ============================================================
# Graphique des performances
# ============================================================

def graphique_ventes(df):
    """
    Affiche la distribution d'une colonne numérique.
    
    Le nom de la fonction est conservé pour rester compatible
    avec le main.py actuel.
    """

    # --------------------------------------------------------
    # Recherche des colonnes numériques
    # --------------------------------------------------------

    colonnes_numeriques = df.select_dtypes(
        include="number"
    ).columns

    # --------------------------------------------------------
    # Vérification de la présence d'une colonne numérique
    # --------------------------------------------------------

    if len(colonnes_numeriques) == 0:

        print(
            "Aucune donnée numérique disponible "
            "pour créer le graphique."
        )

        return

    # --------------------------------------------------------
    # Sélection de la première colonne numérique
    # --------------------------------------------------------

    colonne = colonnes_numeriques[0]

    # --------------------------------------------------------
    # Création du graphique
    # --------------------------------------------------------

    plt.figure(figsize=(10, 5))

    plt.hist(
        df[colonne].dropna(),
        bins=10
    )

    plt.title(
        f"Distribution de {colonne}"
    )

    plt.xlabel(colonne)

    plt.ylabel("Nombre d'étudiants")

    plt.tight_layout()

    plt.show()


# ============================================================
# Graphique des étudiants
# ============================================================

def graphique_etudiants(df):
    """
    Affiche le nombre d'enregistrements par catégorie
    pour une colonne catégorielle.
    """

    # --------------------------------------------------------
    # Recherche des colonnes non numériques
    # --------------------------------------------------------

    colonnes_categorielles = df.select_dtypes(
        exclude="number"
    ).columns

    # --------------------------------------------------------
    # Vérification
    # --------------------------------------------------------

    if len(colonnes_categorielles) == 0:

        print(
            "Aucune colonne catégorielle disponible "
            "pour créer le graphique."
        )

        return

    # --------------------------------------------------------
    # Sélection de la première colonne catégorielle
    # --------------------------------------------------------

    colonne = colonnes_categorielles[0]

    repartition = df[colonne].value_counts()

    # --------------------------------------------------------
    # Création du graphique
    # --------------------------------------------------------

    repartition.plot(
        kind="bar",
        figsize=(10, 5)
    )

    plt.title(
        f"Répartition selon {colonne}"
    )

    plt.xlabel(colonne)

    plt.ylabel("Nombre d'étudiants")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()