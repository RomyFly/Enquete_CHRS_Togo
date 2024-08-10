# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 16:52:51 2024

@author: ok
"""

#Importation des librairies
import sqlite3
import pandas as pd
import streamlit as st

# Création de la connection à la base de données
conn = sqlite3.connect("data_base.db")

#Création du curseur
c = conn.cursor()

#Création de la table

c.execute("""CREATE TABLE IF NOT EXISTS REPONSES (
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pathologie TEXT NOT NULL,
    sexe TEXT NOT NULL,
    date_naissance TEXT NOT NULL,
    niveau_etude TEXT NOT NULL,
    type_profession TEXT NOT NULL,
    nbre_heure_sport_hebdo INTEGER NOT NULL,
    solitude TEXT NOT NULL,
    relation_conflictuelle TEXT NOT NULL,
    meconnaissance_fr_hta TEXT NOT NULL,
    manque_soutien TEXT NOT NULL
    )
           """)          
conn.commit()



#Création de la fonction d'insertion des données dans la table REPONSES de la base de données

def insert_data(pathologie, sexe, date_naissance, niveau_etude,type_profession, 
                nbre_heure_sport_hebdo, solitude, relation_conflictuelle, 
                meconnaissance_fr_hta, manque_soutien):
    c.execute(""" INSERT INTO REPONSES (pathologie, sexe, date_naissance, niveau_etude,type_profession,
                    nbre_heure_sport_hebdo, solitude, relation_conflictuelle,
                    meconnaissance_fr_hta, manque_soutien) VALUES(?,?,?,?,?,?,?,?,?,?)
              """,
              (pathologie, sexe, date_naissance, niveau_etude,type_profession,
                              nbre_heure_sport_hebdo, solitude, relation_conflictuelle,
                              meconnaissance_fr_hta, manque_soutien))
    conn.commit()
    



#Création du formaulaire de saisie des réponses
st.header(':rainbow[Questionnaire sur les socioculturels associés à la décompensation de l’hypertension artérielle]:hospital:', anchor='CENTER')

with st.form("Formulaire"):
    st.subheader(":red[Pathologie]")
    pathologie = st.selectbox("Type d'hypertension artérielle ",["compensée","Décompensée"])
    
    st.subheader(":red[Facteurs sociodémographiques]")
    sexe = st.radio("Sexe",["Masculin","Féminin"])
    date_naissance = st.text_input("Date de naissance (dd-mm-yyyy)")
    niveau_etude = st.selectbox("Niveau d'étude",["Non alphabétisé","Primaire","Secondaire","Universitaire"])
    
    st.subheader(":red[Facteurs socioculturels]")
    type_profession = st.selectbox("Type de profession", ["Physique", "Non physique"])
    nbre_heure_sport_hebdo = st.number_input("Nombre d'heures hebdomadaires d'activités sportives", min_value = 0.0, step = 0.5)
    solitude = st.radio("Vivre en solitude", ["Oui", "Non"])
    relation_conflictuelle = st.radio("Être dans une relation conflictuelle",["Oui","Non"])
    meconnaissance_fr_hta = st.radio("Méconnaissance des facteurs de risques de l’HTA",["Oui","Non"])
    manque_soutien = st.radio("Manque de soutien social et économique",["Oui","Non"])
    
    submit_button = st.form_submit_button("Soumettre!")
    

if submit_button:
    insert_data(pathologie, sexe, date_naissance, niveau_etude,type_profession, 
                    nbre_heure_sport_hebdo, solitude, relation_conflictuelle, 
                    meconnaissance_fr_hta, manque_soutien)
    st.success("Données soumis avec succès!")
    
conn.close()  