import streamlit as st
import pandas as pd
import sqlalchemy
import datetime
import json

import time
import os
import dotenv
dotenv.load_dotenv()


st.set_page_config(page_title="Lista de Compras Inteligente", page_icon=":sparkles:", layout="centered")

st.title("Lista de Compras Inteligente :sparkles:")
st.write("Bem-vindo à Lista de Compras Inteligente! Aqui você pode criar e gerenciar suas listas de compras de forma fácil e eficiente. Adicione itens e programe suas compras. Vamos começar a criar sua lista de compras perfeita!")

st.markdown("### Adicione um item à sua lista de compras")

