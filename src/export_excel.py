# ============================================================
# export_excel.py
#
# Génération d'un rapport Excel professionnel
# ============================================================


import pandas as pd
import os



def exporter_excel(df, chemin):

    """
    Exportation d'un DataFrame vers Excel

    Paramètres :
        df      : données pandas
        chemin  : fichier de sortie
    """



    try:

        # Création du dossier si nécessaire

        dossier = os.path.dirname(chemin)


        if not os.path.exists(dossier):

            os.makedirs(dossier)



        # Création du fichier Excel

        with pd.ExcelWriter(

            chemin,

            engine="openpyxl"

        ) as writer:



            df.to_excel(

                writer,

                sheet_name="Etudiants",

                index=False

            )



            # Statistiques générales

            statistiques = df.describe()



            statistiques.to_excel(

                writer,

                sheet_name="Statistiques"

            )



        print(

            "Excel généré avec succès"

        )



    except Exception as e:


        print(

            "Erreur export Excel :",

            e

        )





# Test

if __name__ == "__main__":


    data = {

        "Nom":["Yao","Sophie"],

        "Moyenne":[85,90]

    }


    df = pd.DataFrame(data)



    exporter_excel(

        df,

        "../reports/Excel/Rapport_Etudiants.xlsx"

    )