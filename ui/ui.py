import streamlit as st
import numpy as np
import plotly.express as px
import sympy as sp
import math
import os
import sys


root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_path not in sys.path:
    sys.path.append(root_path)
    
from methods.bisection import metodo_biseccion
from methods.falsa_posicion import metodo_falsa_posicion
from methods.newton_raphson import newton_raphson
from methods.secante import metodo_secante
from methods.muller import metodo_muller
from methods.trapecio import metodo_trapecio
from methods.simpson import metodo_simpson

st.set_page_config(layout="wide", page_title="Solucionador Numérico", page_icon = "⚛️")

st.title("Solucionador Numérico")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Bisección", "Falsa Posición", "Newton Raphson",
    "Secante", "Müller", "Trapecio", "Simpson", "Acerca de"
])

# ----------------------------------- BISECTION TAB -------------------------------------------------

with tab1:
    col1, col2,col3 = st.columns([1, 1, 1])

    with col1:
        st.subheader("Ingrese los valores de entrada:")
        a = st.number_input("Valor de a", min_value = 0.00001, step = 0.5)
        b = st.number_input("Valor de b", min_value = 0.00001, step = 0.5)
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


# ----------------------------------- FALSE POSITION TAB --------------------------------------------

with tab2:

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.subheader("Ingrese los valores de entrada:")
        a = st.number_input("Valor de a", key="a_tab3")
        b = st.number_input("Valor de b", key="b_tab3")
        funcion = st.text_input("Función", key="funcion_tab3")

        criterio = st.selectbox("Criterio de parada", ["Error Mínimo", "Número de Iteraciones"], key="criterio_tab3")

        if criterio == "Error Mínimo":
            error_minimo = st.text_input("Error Mínimo", key="error_minimo_tab3")
            max_iteraciones = None
        else:
            max_iteraciones = st.text_input("Número de Iteraciones", key="max_iteraciones_tab3")
            error_minimo = None

        st.subheader("Ingrese el rango del gráfico de la función.")
        rang_min_x = st.number_input("Valor -x", key="rang_min_x_tab3")
        rang_max_x = st.number_input("Valor +x", key="rang_max_x_tab3")

        if st.button("Calcular", key="calcular_tab3"):
            try:
                error_minimo = float(error_minimo) if error_minimo else None
                max_iteraciones = int(max_iteraciones) if max_iteraciones else None

                # Llamar al método de falsa posición en lugar de bisección
                iteraciones, raiz, error_final, lista_iteraciones = metodo_falsa_posicion(a, b, funcion, error_minimo, max_iteraciones)

                with col2:
                    st.subheader("Resultados del Método")
                    st.write("Método: Falsa Posición")
                    st.write(f"Número de iteraciones: {iteraciones}")
                    st.write(f"La raíz del método es: {format(raiz, '.3f')}")
                    st.write(f"Error final: {format(error_final, '.3f')}%")

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

with tab3:

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:

        st.subheader("Ingrese los valores de entrada: ")
        new_x = st.number_input("Valor Inicial")
        funcion = st.text_input("Función", key = "new_rap")
        criterio = st.selectbox("Criterio de Parada", ["Número de Iteraciones","Error Mínimo"])

        if criterio == "Número de Iteraciones":

            max_iteraciones = st.number_input("Número de Iteraciones")
            error_minimo = None

        elif criterio == "Error Mínimo":

            error_minimo = st.number_input("Error Mínimo")
            max_iteraciones = None

        st.subheader("Ingrese el rango del gráfico de la función.")
        rang_min_x = st.number_input("Valor -x", key = "-x_new_rap")
        rang_max_x = st.number_input("Valor +x", key = "+x_new_rap")

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

# ----------------------------------- SECANT TAB ----------------------------------------------------

with tab4:
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.subheader("Ingrese los valores de entrada: ")
        x0 = st.number_input("Valor Inicial x0")
        x1 = st.number_input("Valor Inicial x1")
        funcion = st.text_input("Función", key="secant")
        criterio = st.selectbox("Criterio de Parada", ["Número de Iteraciones", "Error Mínimo"], key="secant_criterio")

        if criterio == "Número de Iteraciones":
            max_iteraciones = st.number_input("Número de Iteraciones", key="max_iteraciones_secant")
            error_minimo = None
        elif criterio == "Error Mínimo":
            error_minimo = st.number_input("Error Mínimo")
            max_iteraciones = None

        st.subheader("Ingrese el rango del gráfico de la función.")
        rang_min_x = st.number_input("Valor -x", key="-x_secant")
        rang_max_x = st.number_input("Valor +x", key="+x_secant")

        st.divider()

        if st.button("Calcular", key="secant_btn"):
            try:
                list_its, est_err, raiz = metodo_secante(x0, x1, funcion, max_iteraciones, error_minimo)

                with col2:
                    st.subheader("Resultados del Método")
                    st.write("Método: Secante")
                    st.write(f"Número de iteraciones: {len(list_its) - 1}")
                    st.write(f"La raíz del método es: {format(raiz, '.5f')}")
                    st.write(f"Error final: {format(est_err, '.3f')}%")

                    st.subheader("Función")
                    lat_expression = funcion.replace("**", "^").replace("*", " ").replace("math.exp", "e^")
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
                    st.dataframe(list_its)

            except Exception as e:
                st.error(f"Error en el cálculo: {str(e)}")

# ----------------------------------- MÜLLER TAB ----------------------------------------------------

with tab5:
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.subheader("Ingrese los valores de entrada: ")
        x0 = st.number_input("Valor Inicial x0", key="x0_muller")
        x1 = st.number_input("Valor Inicial x1", key="x1_muller")
        x2 = st.number_input("Valor Inicial x2", key="x2_muller")
        funcion = st.text_input("Función", key="muller")
        criterio = st.selectbox("Criterio de Parada", ["Número de Iteraciones", "Error Mínimo"], key="muller_criterio")

        if criterio == "Número de Iteraciones":
            max_iteraciones = st.number_input("Número de Iteraciones", key="max_iteraciones_muller")
            error_minimo = None
        elif criterio == "Error Mínimo":
            error_minimo = st.number_input("Error Mínimo", key="error_minimo_muller")
            max_iteraciones = None

        st.subheader("Ingrese el rango del gráfico de la función.")
        rang_min_x = st.number_input("Valor -x", key="-x_muller")
        rang_max_x = st.number_input("Valor +x", key="+x_muller")

        st.divider()

        if st.button("Calcular", key="muller_btn"):
            try:
                list_its, est_err, raiz = metodo_muller(x0, x1, x2, funcion, max_iteraciones, error_minimo)

                with col2:
                    st.subheader("Resultados del Método")
                    st.write("Método: Muller")
                    st.write(f"Número de iteraciones: {len(list_its) - 1}")
                    st.write(f"La raíz del método es: {format(raiz, '.5f')}")
                    st.write(f"Error final: {format(est_err, '.3f')}%")

                    st.subheader("Función")
                    lat_expression = funcion.replace("**", "^").replace("*", " ").replace("math.exp", "e^")
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
                    st.dataframe(list_its)

            except Exception as e:
                st.error(f"Error en el cálculo: {str(e)}")

# # ----------------------------------- TAYLOR SERIES TAB --------------------------------------------

# def serie_taylor(funcion, x0, n, punto):
#     x = sp.Symbol('x')
#     f = sp.sympify(funcion)
#     serie = 0

#     for i in range(n+1):
#         derivada = sp.diff(f, x, i)
#         termino = (derivada.subs(x, x0) * (punto - x0)**i) / math.factorial(i)
#         serie += termino

#     return float(serie)

# with tab6:
#     col1, col2 = st.columns([1, 2])

#     with col1:
#         st.subheader("Ingrese los valores de entrada:")
#         funcion = st.text_input("Función", key="taylor_fun")
#         x0 = st.number_input("(x₀)", key="taylor_x0")
#         n = st.number_input("n", min_value=1, value=4, key="taylor_n")
#         punto = st.number_input("Punto a evaluar", key="taylor_punto")

#         if st.button("Calcular", key="taylor_btn"):
#             try:
#                 resultado = serie_taylor(funcion, x0, n, punto)

#                 with col2:
#                     st.subheader("Resultados")
#                     st.write(f"Valor aproximado en x = {punto}: {resultado}")

#                     x = sp.Symbol('x')
#                     f = sp.sympify(funcion)
#                     valor_real = float(f.subs(x, punto))
#                     error = abs((valor_real - resultado)/valor_real) * 100

#                     st.write(f"Valor real: {valor_real}")
#                     st.write(f"Error relativo: {error:.2f}%")

#             except Exception as e:
#                 st.error(f"Error en el cálculo: {str(e)}")

# # ----------------------------------- MACLAURIN SERIES TAB --------------------------------------------

# def serie_maclaurin(funcion, n, punto):
#     return serie_taylor(funcion, 0, n, punto)

# with tab7:
#     col1, col2 = st.columns([1, 2])

#     with col1:
#         st.subheader("Ingrese los valores de entrada:")
#         funcion = st.text_input("Función", key="maclaurin_fun")
#         n = st.number_input("n", min_value=1, value=4, key="maclaurin_n")
#         punto = st.number_input("Punto a evaluar", key="maclaurin_punto")

#         if st.button("Calcular", key="maclaurin_btn"):
#             try:
#                 resultado = serie_maclaurin(funcion, n, punto)

#                 with col2:
#                     st.subheader("Resultados")
#                     st.write(f"Valor aproximado en x = {punto}: {resultado}")

#                     x = sp.Symbol('x')
#                     f = sp.sympify(funcion)
#                     valor_real = float(f.subs(x, punto))
#                     error = abs((valor_real - resultado)/valor_real) * 100

#                     st.write(f"Valor real: {valor_real}")
#                     st.write(f"Error relativo: {error:.2f}%")

#             except Exception as e:
#                 st.error(f"Error en el cálculo: {str(e)}")

# ----------------------------------- TRAPEZOIDAL RULE TAB --------------------------------------------

with tab6:
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.subheader("Ingrese los valores de entrada:")
        funcion = st.text_input("Función", key="trap_fun")
        a = st.number_input("Límite inferior", key="trap_a")
        b = st.number_input("Límite superior", key="trap_b")
        n = st.number_input("Número de subintervalos", min_value=1, value=4, key="trap_n")

        if st.button("Calcular", key="trap_btn"):
            try:
                resultado, intervals = metodo_trapecio(funcion, a, b, n)

                with col2:
                    st.subheader("Resultados")
                    st.write(f"Valor de la integral: {resultado:.6f}")

                    st.subheader("Función")
                    lat_expression = funcion.replace("**", "^").replace("*", " ")
                    st.latex(lat_expression)

                    st.subheader("Gráfico de la función")
                    x = np.linspace(a, b, 200)
                    y = [eval(funcion) for x in x]

                    fig = px.line(x=x, y=y, title='Función')
                    fig.update_layout(template='plotly_dark')
                    st.plotly_chart(fig, use_container_width=True)

                with col3:
                    st.subheader("Tabla de valores")
                    simple_intervals = [[i+1, float(intervals[i][1]), float(intervals[i][2])]
                                     for i in range(len(intervals))]
                    st.dataframe(simple_intervals,
                               column_config={
                                   0: "Iteración",
                                   1: "x",
                                   2: "f(x)"
                               })

            except Exception as e:
                st.error(f"Error en el cálculo: {str(e)}")

# ----------------------------------- SIMPSON'S RULE TAB --------------------------------------------

with tab7:
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.subheader("Ingrese los valores de entrada:")
        funcion = st.text_input("Función", key="simp_fun")
        a = st.number_input("Límite inferior", key="simp_a")
        b = st.number_input("Límite superior", key="simp_b")
        n = st.number_input("Número de subintervalos (par)", min_value=2, value=4, step=2, key="simp_n")

        if st.button("Calcular", key="simp_btn"):
            try:
                resultado, intervals = metodo_simpson(funcion, a, b, n)

                with col2:
                    st.subheader("Resultados")
                    st.write(f"Valor de la integral: {resultado:.6f}")

                    st.subheader("Función")
                    lat_expression = funcion.replace("**", "^").replace("*", " ")
                    st.latex(lat_expression)

                    st.subheader("Gráfico de la función")
                    x = np.linspace(a, b, 200)
                    y = [eval(funcion) for x in x]

                    fig = px.line(x=x, y=y, title='Función')
                    fig.update_layout(template='plotly_dark')
                    st.plotly_chart(fig, use_container_width=True)

                with col3:
                    st.subheader("Tabla de valores")
                    simple_intervals = [[i+1, float(intervals[i][1]), float(intervals[i][2])]
                                     for i in range(len(intervals))]
                    st.dataframe(simple_intervals,
                               column_config={
                                   0: "Iteración",
                                   1: "x",
                                   2: "f(x)"
                               })

            except Exception as e:
                st.error(f"Error en el cálculo: {str(e)}")

# ----------------------------------- ABOUT TAB ----------------------------------------------------

with tab8:

    ...
    # col1, col2, col3 = st.columns([1, 1, 1])

    # with col2:
    #     st.subheader("Acerca de")

    #     st.write("""
    #     Este proyecto de Streamlit fue desarrollado como parte del curso de **Análisis Numérico**. Permite calcular raíces de funciones mediante diferentes métodos numéricos, optimizando el proceso de cálculo y facilitando el análisis de resultados.
    #     """)

    #     st.write("""
    #     **Equipo de desarrollo**
    #     - **Mateo Vergara**: Desarrollo de software y programación en Streamlit.
    #     - **Maria Paula Paredes Lozada** y **Lya Velez Pineda**: Organización y conversión de métodos a algoritmos numéricos, así como la documentación del proyecto.
    #     """)