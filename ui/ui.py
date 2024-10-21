import streamlit as st
import numpy as np
import plotly.express as px
import sympy as sp
import math
from pprint import pprint



st.set_page_config(layout="wide")

st.title("Solucionador Numérico")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Bisección", "Newton Raphson", "Falsa Posición", 
    "Secante", "Müller", "Series de Taylor", "Serie de Maclaurin"
])

# ----------------------------------- BISECTION TAB -------------------------------------------------

def metodo_biseccion(a, b, funcion, error_minimo=None, max_iteraciones=None):
    def evaluar_funcion(x):
        return eval(funcion)
    
    c = (a + b) / 2
    est_error = 100 
    list_vals = [a, b, c, est_error]
    list_its = [list_vals]
    new_itr = 0
    
    while True:
        new_list = [evaluar_funcion(x) for x in list_vals[:3]]
        
        if (new_list[0] * new_list[2]) < 0:
            list_vals = [list_vals[0], list_vals[2]]
        elif (new_list[0] * new_list[2]) > 0:
            list_vals = [list_vals[2], list_vals[1]]
        else:
            break  # Se encontró la raíz exacta
        
        list_vals.append((list_vals[0] + list_vals[1]) / 2)
        new_c = list_vals[2]
        old_c = list_its[new_itr][2]
        est_error = abs((new_c - old_c) / new_c) * 100
        list_vals.append(est_error)
        list_its.append(list_vals)
        new_itr += 1
        
        if error_minimo is not None and est_error <= error_minimo:
            break
        if max_iteraciones is not None and new_itr >= max_iteraciones:
            break
    
    return new_itr + 1, list_vals[2], est_error, list_its

with tab1:
    col1, col2,col3 = st.columns([1, 1, 1])
    
    with col1:
        st.subheader("Ingrese los valores de entrada:")
        a = st.number_input("Valor de a")
        b = st.number_input("Valor de b")
        funcion = st.text_input("Función")
        
        criterio = st.selectbox("Criterio de parada", ["Error Mínimo", "Número de Iteraciones"])
        
        if criterio == "Error Mínimo":
            error_minimo = st.text_input("Error Mínimo")
            max_iteraciones = None
        else:
            max_iteraciones = st.text_input("Número de Iteraciones")
            error_minimo = None

        st.subheader("Ingrese el rango del gráfico de la función.")
        rang_min_x = st.number_input("Valor -x")
        rang_max_x = st.number_input("Valor +x")
        
        if st.button("Calcular"):
            try:

                error_minimo = float(error_minimo) if error_minimo else None
                max_iteraciones = int(max_iteraciones) if max_iteraciones else None
                
                iteraciones, raiz, error_final, lista_iteraciones = metodo_biseccion(a, b, funcion, error_minimo, max_iteraciones)
                
                with col2:
                    st.subheader("Resultados del Método")
                    st.write("Método: Bisección")
                    st.write(f"Número de iteraciones: {iteraciones}")
                    st.write(f"La raíz del método es: {format(raiz, ".3f")}")
                    st.write(f"Error final: {format(error_final, ".3f")}%")
                    
                    st.subheader("Función")
                    lat_expression = funcion.replace("**", "^").replace("*", " ")
                    st.latex(lat_expression)
                    
                    st.subheader("Gráfico de la función")
                    x = np.linspace(rang_min_x, rang_max_x, 100)
                    y = [eval(funcion) for x in x]
                    
                    fig = px.line(x=x, y=y, labels={'x': 'x', 'y': 'f(x)'}, title=' ')
                    fig.add_scatter(x=[raiz], y=[0], mode='markers', name='Raíz')
                    fig.update_layout(template='plotly_dark')
                    st.plotly_chart(fig, use_container_width=True)
                
                with col3:
                                        
                    st.subheader("Tabla de iteraciones")
                    st.dataframe(lista_iteraciones)
            
            except Exception as e:
                st.error(f"Error en el cálculo: {str(e)}")
                

# ----------------------------------- NEWTON RAPHSON TAB --------------------------------------------

def newton_raphson(new_x, funcion, max_iters=None, min_error=None):
    
    x = sp.Symbol('x')
    deri = sp.diff(funcion, x)
    
    evaluar_funcion = sp.lambdify(x, funcion)
    evaluar_derivada = sp.lambdify(x, deri)
    
    iters = 0 # Contador de iteraciones
    est_err = 100 # Error inicial


    list_its = [[iters, new_x, est_err]]  # Lista para todas las iteraciones
    iter_list = [] # Lista para la iteración actual

    while True: 
    
        old_x = new_x
        new_x = new_x - (evaluar_funcion(new_x) / evaluar_derivada(new_x))
        est_err = abs((new_x - old_x) / new_x) * 100
        
        iter_list.append(iters+1)
        iter_list.append(format(new_x, ".5f"))
        iter_list.append(format(est_err,".3f"))
        list_its.append(iter_list.copy())
        
        iters += 1
        iter_list.clear()
        
        if min_error is not None and est_err < min_error:
            break
        
        if max_iters is not None and iters >= max_iters:
            break
    
    return list_its, est_err, new_x


with tab2: 
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        
        st.subheader("Ingrese los valores de entrada: ")
        new_x = st.number_input("Valor Inicial")
        funcion = st.text_input("Función", key="new_rap")
        criterio = st.selectbox("Criterio de Parada", ["Número de Iteraciones","Error Mínimo"])
        
        if criterio == "Número de Iteraciones":
            
            max_iteraciones = st.number_input("Número de Iteraciones")
            error_minimo = None
            
        elif criterio == "Error Mínimo":
            
            error_minimo = st.number_input("Error Mínimo")
            max_iteraciones = None
        
        st.subheader("Ingrese el rango del gráfico de la función.")
        rang_min_x = st.number_input("Valor -x", key="-x_new_rap")
        rang_max_x = st.number_input("Valor +x", key="+x_new_rap")
        
        st.divider()
        
        if st.button("Calcular", key="new_rap_btn"):
            
            try: 
                
                list_its, est_err, raiz = newton_raphson(new_x, funcion, max_iteraciones, error_minimo)
                
                
                with col2:
                    
                    st.subheader("Resultados del Método")
                    st.write("Método: Newton Raphson")
                    st.write(f"Número de iteraciones: {len(list_its)}")
                    st.write(f"La raíz del método es: {format(raiz, ".5f")}")
                    st.write(f"Error final: {format(est_err, ".3f")}%")
                    
                    st.subheader("Función")
                    lat_expression = funcion.replace("**", "^").replace("*", " ")
                    st.latex(lat_expression)
                    
                    st.subheader("Derivada")
                    x = sp.Symbol('x')
                    deri = sp.diff(funcion, x)
                    lat_expression_2 = deri
                    st.latex(lat_expression_2)
                    
                    st.subheader("Gráfico de la función")
                    x = np.linspace(rang_min_x, rang_max_x, 100)
                    y = [eval(funcion) for x in x]
                    
                    fig = px.line(x=x, y=y, labels={'x': 'x', 'y': 'f(x)'}, title=' ')
                    fig.add_scatter(x=[raiz], y=[0], mode='markers', name='Raíz')
                    fig.update_layout(template='plotly_dark')
                    st.plotly_chart(fig, use_container_width=True)
                    
                with col3:
                    
                    st.subheader("Tabla de iteraciones")
                    st.dataframe(list_its)
                    
            except Exception as e:
                st.error(f"Error en el cálculo: {str(e)}")