'''
testando o pandas e o venv

principais comandos venv:
    python3 -m venv .venv
    source .venv/bin/activate

criando requirements.txt:
    pip freeze >> requirements.txt

inicializando o streamlit:
    streamlit run trabalhando_com_pandas.py
'''
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first_column'  :    [1,2,3],
    'second_column' :    [4,5,6]
})

st.write("Meu App")
df