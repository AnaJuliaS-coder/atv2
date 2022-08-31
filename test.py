import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

t = np.linspace(0, 0.05, 1000)
v = 220 * np.sqrt(2) * np.sin(2 * np.pi * 60 * t)
v1 = (220 * np.sqrt(2) * np.sin(2 * np.pi * 60 * t))**2
fig1 = go.Figure(data=go.Scatter(x=t, y=v))
fig2 = go.Figure(data=go.Scatter(x=t, y=v1))

st.markdown("# Site criado engenheira de petróleo Ana Júlia")
st.markdown("## Primerio gráfico")
st.markdown("Função --> $200*√2*sin(2*π*60*t)$")
st.plotly_chart(fig1)
st.markdown("## Segundo gráfico")
st.markdown("Função --> $[200*√2*√sin(2*π*60*t)]^2$")
st.plotly_chart(fig2)