# ============================================================
# export_pdf.py
#
# Création d'un rapport PDF automatique
# ============================================================


from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer,

    Table,

    TableStyle

)


from reportlab.lib.styles import getSampleStyleSheet



import pandas as pd




def creer_pdf(df, fichier):


    document = SimpleDocTemplate(

        fichier

    )


    elements=[]



    styles = getSampleStyleSheet()



    titre = Paragraph(

        "Rapport Analyse des Etudiants",

        styles["Title"]

    )


    elements.append(titre)



    elements.append(

        Spacer(1,20)

    )



    texte = Paragraph(

        f"""

        Nombre total d'étudiants :

        {len(df)}

        """,

        styles["Normal"]

    )


    elements.append(texte)



    elements.append(

        Spacer(1,20)

    )



    # Tableau résumé

    data = [

        list(df.columns)

    ]



    for ligne in df.head(10).values.tolist():

        data.append(ligne)



    table = Table(data)



    table.setStyle(

        TableStyle([

            ('GRID',

             (0,0),

             (-1,-1),

             1,

             None)

        ])

    )



    elements.append(table)



    document.build(elements)



    print(

        "PDF créé"

    )





if __name__ == "__main__":


    df=pd.DataFrame({

        "Nom":["Yao","Julie"],

        "Moyenne":[85,92]

    })



    creer_pdf(

        df,

        "../reports/PDF/Rapport_Analyse.pdf"

    )