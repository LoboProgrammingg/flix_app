import streamlit as st
import pandas as pd
import numpy as np


st.title('Flix App')
st.divider()
st.text_input('Nome do Filme:')
st.button('Salvar')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)