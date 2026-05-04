import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Cargamos la configuración del archivo .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configuración visual de la página
st.set_page_config(page_title="RandomCAR.com", page_icon="🚗", layout="centered")

# Verificamos que la API KEY esté presente
if not api_key:
    st.error("❌ No se encontró la GOOGLE_API_KEY en el archivo .env")
    st.stop()

# Configuramos el motor de IA de Google
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Interfaz de usuario
st.title("🚗 RandomCAR: Inteligencia Automotriz")
st.markdown("---")
st.subheader("Consulta con el Experto")

pregunta = st.text_input("Escribe tu duda técnica (ej. ¿Cómo calibrar un motor?)", placeholder="¿En qué puedo ayudarte hoy?")

if st.button("Enviar Consulta"):
    if pregunta:
        with st.spinner("Analizando componentes..."):
            try:
                # Personalizamos la respuesta para tu marca KusanagiGear / RandomCAR
                prompt_ingeniero = f"Eres un experto en ingeniería automotriz de RandomCAR. Responde de forma técnica y profesional a: {pregunta}"
                response = model.generate_content(prompt_ingeniero)
                
                st.success("Análisis completado:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error técnico: {e}")
    else:
        st.warning("Por favor, introduce una pregunta.")

# Pie de página con tu marca
st.markdown("---")
st.caption("© 2026 RandomCAR.com | Desarrollado por Pepe - Futuro Ingeniero en Sistemas")