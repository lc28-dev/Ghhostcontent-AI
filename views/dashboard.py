import streamlit as st
from src.ai_engine import generate_social_bundle

def show():
    st.title("🚀 Créateur de contenu")
    
    with st.form("gen_form"):
        biz = st.text_input("Nom de votre commerce")
        industry = st.selectbox("Secteur", ["Restaurant", "Immobilier", "Beauté", "Sport"])
        goal = st.selectbox("Objectif", ["Plus de clients", "Plus de vues", "Vendre un produit"])
        submitted = st.form_submit_button("✨ Générer mon contenu")
        
    if submitted:
        with st.spinner("L'IA travaille..."):
            result = generate_social_bundle(biz, industry, "Professionnel", goal)
            st.success("Terminé !")
            st.write(result)
