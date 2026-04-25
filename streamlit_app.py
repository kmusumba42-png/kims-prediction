import streamlit as st
from datetime import datetime
st.set_page_config(page_title="KIMS PRÉDICTION")
st.title("⚽ KIMS PRÉDICTION")
st.write("### Expertise de **KimsFélicité**")
st.sidebar.info("Partenaire : Félicité KILOLO MUSUMBA")
choix = st.selectbox("Menu",["VALUE BETS","COUPONS","PAYEMENT","ADMIN"])
if choix == "VALUE BETS":
 st.header("Analyse")
  st.date_input("Date",datetime.now())
   if st.button("Lancer"):
     st.info("Recherche...")
     if choix == "COUPONS":
      st.header("Espace Coupons")
       st.success("🎫 COUPON GRATUIT disponible")
        st.warning("🎫 COUPON PREMIUM : VIP")
        if choix == "PAYEMENT":
         st.header("Abonnements")
          st.write("M-Pesa : +243 816 272 212")
           st.write("Airtel : +243 996 660 000")
            st.write("Orange : +243 855 415 399")
            if choix == "ADMIN":
             st.header("Contrôle")
              psw = st.text_input("Code",type="password")
               if psw == "243":
                 st.success("Bienvenue, Partenaire")
                 