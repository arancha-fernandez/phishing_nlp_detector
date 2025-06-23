
import streamlit as st
import spacy
from utils import analyze_text

st.set_page_config(page_title="Analizador de Amenazas", layout="wide")

st.title("🔍 Analizador Inteligente de Amenazas en Comunicaciones")

user_input = st.text_area("Pega aquí el texto del correo o mensaje sospechoso", height=300)

if st.button("Analizar"):
    if user_input.strip():
        result = analyze_text(user_input)
        st.markdown(f"## Resultado del análisis")
        st.markdown(f"**Nivel de Riesgo:** {result['risk_level']}")
        st.markdown("### Detalles:")
        for issue in result['issues']:
            st.markdown(f"- {issue}")
    else:
        st.warning("Por favor, introduce un texto para analizar.")
