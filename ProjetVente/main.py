from extract import extract_data
from transform import transform_data
from analyse import statistiques
from load import load_data


def main():

    print("===== PIPELINE ETL =====")

    # Extraction
    df = extract_data(
        "D:/Git/Projet_ETL_ventes/data/ventes.csv"
    )

    # Transformation
    df = transform_data(df)

    # Analyse
    resultats = statistiques(df)

    print("\n===== KPI =====")

    for nom, valeur in resultats.items():
        print(f"{nom} : {valeur:.2f}")

    # Chargement
    load_data(df)

    print("\n===== PIPELINE TERMINÉ =====")


if __name__ == "__main__":
    main()