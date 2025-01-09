import streamlit as st
from transformers import pipeline

generacion_texto = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

st.title("Preguntas y Respuestas")
question = st.text_input("Pregunta:")

if st.button("Obtener Respuesta"):
    prompt = f"Contexto: eres un asistente que responde preguntas sencillas:\nPregunta: {question}\nRespuesta:"
    result = generacion_texto(prompt, max_length=150, num_return_sequences=1)
    st.write(result[0]['generated_text'].split("Respuesta:")[1].strip())