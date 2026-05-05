import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Cargar configuración
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Configurar IA
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Falta la GOOGLE_API_KEY. Configúrala en Secrets o archivo .env")

# 3. Interfaz
st.title("🚗 RandomCAR.com")
st.subheader("Inteligencia Automotriz by Pepe")

pregunta = st.text_input("¿Qué duda tienes sobre tu auto?")

if st.button("Consultar"):
    if pregunta and api_key:
        with st.spinner("Pensando..."):
            response = model.generate_content(pregunta)
            st.success(response.text)
