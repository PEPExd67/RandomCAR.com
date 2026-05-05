import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Configuración de página
st.set_page_config(page_title="RandomCAR.com", page_icon="🚗")

# Cargar API Key (Localmente del .env, en la nube de 'Secrets')
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.title("🚗 RandomCAR: Inteligencia Automotriz")
    st.markdown("---")
    
    pregunta = st.text_input("Hazle una pregunta técnica al experto:")

    if st.button("Consultar"):
        if pregunta:
            with st.spinner("Analizando componentes..."):
                try:
                    response = model.generate_content(f"Actúa como un experto mecánico profesional. Responde a: {pregunta}")
                    st.success(response.text)
                except Exception as e:
                    st.error(f"Error de conexión: {e}")
else:
    st.error("Falta la configuración de la API Key.")

st.markdown("---")
st.caption("© 2026 RandomCAR.com | Desarrollado por Pepe - Futuro Ingeniero en Sistemas")