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
conn.close()


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