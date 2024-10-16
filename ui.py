import streamlit as st
import numpy as np
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Solucionador Numérico")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Bisección", "Falsa Posición", "Newton Raphson", 
    "Secante", "Müller", "Series de Taylor", "Serie de Maclaurin"
])

with tab1:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Ingrese los valores de entrada")
        st.text_input("Valor de a")
        st.text_input("Valor de b")
        st.text_input("Función")
        st.text_input("Entrada n")
        
        st.button("Calcular")
    
    with col2:
        st.subheader("Resultados del Método")
        st.write("Método: Bisección")
        st.write("Número de iteraciones hasta error menor a [min_est_error]%")
        st.write("La raíz del método es: [raíz]")
        
        st.subheader("Gráfico de la función")
        
        x = np.linspace(0, 2*np.pi, 100)
        y = np.cos(x)
        
        fig = px.line(x=x, y=y, labels={'x': 'θ', 'y': 'g(θ)'}, title='g(θ) = cos(θ)')
        
        fig.update_layout(template='plotly_white')

        st.plotly_chart(fig, use_container_width=True)