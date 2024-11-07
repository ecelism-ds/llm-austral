import streamlit as st

import os
import json
os.environ["OPENAI_API_KEY"] = ''
from openai import OpenAI
client = OpenAI()

def get_summary(chunk, previous_summary=None):
    prompt = f"""
    Summarize the following conversation between two people. Highlight any key moments and characterize their relationship.
    For every conclusion you arrive, extract a piece of text that support that conclussion.
    You are going to be provided a "previous sumup" with the sumup up to the part you are analyzing and the "current part", the part that you are analyzing.
    PREVIOUS SUMUP:
    {previous_summary if previous_summary else ''}
    CURRENT PART:
    {chunk}
    """.strip()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes conversations and extracts important details."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

st.set_page_config(
    page_title="My App",
    page_icon="🧐",
    layout="centered",
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([1, 4])
with col1:
    st.image("./TP2/whatsappanalyzer/logo.jpg", use_column_width=True)
with col2:
    st.title('Whatsapp Analyzer')

instrucciones = """
### Instrucciones
1. Descargar el historial de conversaciones de whatsapp a analizar siguiendo los pasos de [Download Conversation Whatsapp History](https://faq.whatsapp.com/1180414079177245/?locale=et_EE&cms_platform=android)
2. Subirlo (ver abajo). Para eso van a tener que pasarlo a la computadora donde estén usando esta página. Pueden mandárselo por mail a ustedes mismos.
3. Esperar a que se complete el análisis.
"""
st.write(instrucciones)
uploaded_file = st.file_uploader("Upload the whatsapp dump: ", type=["txt", "csv", "pdf", "png", "jpg"])


if uploaded_file is not None:
    # Process based on file type
    if uploaded_file.type == "text/plain":
        conversation = uploaded_file.read().decode("utf-8").split('\n')
        chunk_size = 200
        sumups = [""]
        progress = st.markdown("Progress: 0%")
        progress_bar = st.progress(0)
        st.markdown("# Generated sumup:") 
        for i in range(0,len(conversation),chunk_size):
            
            message_chunk = '\n'.join(conversation[i:i+chunk_size])
            sumups.append(get_summary(message_chunk, previous_summary=sumups[-1]))
            ratio = (i+1)/len(conversation)
            print(sumups[-1])
            st.markdown(sumups[-1])    
            progress_bar.progress(ratio)
            progress.markdown(f"Progress: {ratio*100:.2f}%")
        progress_bar.progress(1.0)
        progress.markdown(f"Progress: 100%")

