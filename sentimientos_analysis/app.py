import streamlit as st
from transformers import pipeline

sentimientos_analysis = pipeline("sentiment-analysis")

st.title("Análisis de los Sentimientos")
user_input = st.text_area("Introduce un texto para analizar:")

if st.button("Analizar"):
    result = sentimientos_analysis(user_input)
    st.write(result) 