import streamlit as st
from datetime import datetime

# CONFIGURATION
st.set_page_config(page_title="KIMS PRÉDICTION")

# IDENTITÉ
st.title("⚽ KIMS PRÉDICTION")
st.write("### Expertise de **KimsFélicité**")
st.sidebar.info("Partenaire : Félicité KILOLO MUSUMBA")

# MENU SIMPLE
choix = st.selectbox("Menu", ["VALUE BETS", "COUPONS", "PAYEMENT", "ADMIN"])

# 1. VALUE BETS
if choix == "VALUE BETS":
 st.header("Analyse des Matchs")
  st.date_input("Choisir une date", datetime.now())
   if st.button("Lancer l'Analyse"):
     st.info("Recherche de Value Bets en cours...")

     # 2. COUPONS
     if choix == "COUPONS":
      st.header("Espace Coupons")
       st.success("🎫 COUPON GRATUIT : Disponible")
        st.warning("🎫 COUPON PREMIUM : Réservé aux VIP")

        # 3. PAYEMENT
        if choix == "PAYEMENT":
         st.header("Abonnements Premium")
          st.write("M-Pesa : +243 816 272 212")
           st.write("Airtel : +243 996 660 000")
            st.write("Orange : +243 855 415 399")
             st.write("Tarifs : 3000 FC (Semaine) | 12000 FC (Mois)")

             # 4. ADMIN
             if choix == "ADMIN":
              st.header("Contrôle Partenaire")
               psw = st.text_input("Code Secret", type="password")
                if psw == "243":
                  st.success("### Bienvenue, Partenaire Félicité KILOLO MUSUMBA")
