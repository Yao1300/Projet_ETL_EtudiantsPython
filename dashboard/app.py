# ============================================================
# Dashboard étudiants avec Streamlit
# ============================================================


import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns




st.set_page_config(

    page_title="Dashboard étudiants",

    layout="wide"

)



st.title(

    "📊 Dashboard Analyse des étudiants"

)



# Chargement données

df = pd.read_csv(

    "../data/Etudiants_final.csv"

)



st.sidebar.header(

    "Filtres"

)



ville = st.sidebar.selectbox(

    "Choisir une ville",

    df["Ville"].unique()

)



df_filtre = df[

    df["Ville"]==ville

]



# KPI


col1,col2,col3 = st.columns(3)



col1.metric(

    "Nombre étudiants",

    len(df_filtre)

)



col2.metric(

    "Moyenne",

    round(df_filtre["Moyenne"].mean(),2)

)



col3.metric(

    "Age moyen",

    round(df_filtre["Age"].mean(),1)

)





# Graphique


st.subheader(

    "Distribution des moyennes"

)



fig,ax = plt.subplots()



sns.histplot(

    df_filtre["Moyenne"],

    kde=True,

    ax=ax

)



st.pyplot(fig)



st.subheader(

    "Données"

)


st.dataframe(

    df_filtre

)