import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="KIMS PRÉDICTION", page_icon="⚽")

st.title("⚽ KIMS PRÉDICTION")
st.markdown("---")

# Vos informations d'accès
API_KEY = "32e1ac42d16fe9a4d0c48a17398f74b5"
HEADERS = {'x-rapidapi-key': API_KEY, 'x-rapidapi-host': 'v3.football.api-sports.io'}

# Interface utilisateur
date_sel = st.date_input("Choisir une date pour l'analyse", datetime.now())

if st.button("Lancer l'Analyse"):
    url = f"https://v3.football.api-sports.io/fixtures?date={date_sel.strftime('%Y-%m-%d')}"
    
    with st.spinner('Analyse des matchs en cours...'):
        try:
            r = requests.get(url, headers=HEADERS).json()
            matchs = r.get('response', [])
            
            if matchs:
                st.success(f"{len(matchs)} matchs trouvés !")
                for m in matchs[:15]:
                    equipes = f"🏟️ {m['teams']['home']['name']} vs {m['teams']['away']['name']}"
                    st.write(equipes)
            else:
                st.warning("Aucun match trouvé pour cette date.")
        except:
            st.error("Erreur de connexion. Vérifiez votre clé API.")

st.sidebar.markdown("### Application Officielle")
st.sidebar.info("Gérée par KimsFélicité")
                                   
