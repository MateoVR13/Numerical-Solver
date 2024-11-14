import sympy as sp
import math

def serie_taylor(funcion, x0, n, punto):
    x = sp.Symbol('x')
    f = sp.sympify(funcion)
    serie = 0
    
    for i in range(n+1):
        derivada = sp.diff(f, x, i)
        termino = (derivada.subs(x, x0) * (punto - x0)**i) / math.factorial(i)
        serie += termino
    
    return float(serie)
