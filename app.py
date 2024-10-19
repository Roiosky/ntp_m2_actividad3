import streamlit as st
import pandas as pd

st.title("Visualizador de Datos CSV")

uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Lee el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv(uploaded_file)

    st.table(df)

