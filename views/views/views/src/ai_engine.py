import openai
import os
import json

def generate_social_bundle(business_name, industry, tone, goal):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"Crée 3 posts Instagram et 1 calendrier pour {business_name} dans le secteur {industry}. Objectif: {goal}."
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except:
        return "Erreur : Configurez votre clé API OpenAI dans les secrets Streamlit."
