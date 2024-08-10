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

c.execute("""CREATE TABLE IF NOT EXISTS RESPONSES (
    
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pathologie TEXT NOT NULL,
    sexe TEXT NOT NULL,
    age INTEGER NOT NULL,
    niveau_etude TEXT NOT NULL,
    situation_matrimoniale TEXT NOT NULL,
    solitude TEXT NOT NULL,
    relation_conflictuelle TEXT NOT NULL,
    meconnaissance_fr_hta TEXT NOT NULL,
    manque de soutien TEXT NOT NULL,
    conception_mystique_hta text NOT NULL
    )
           """)
           
conn.commit()
conn.close()
