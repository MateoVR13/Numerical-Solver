import sympy as sp
from pprint import pprint

def newton_raphson(new_x, funcion, max_iters=None, min_error=None):
    
    x = sp.Symbol('x')
    deri = sp.diff(funcion, x)
    
    evaluar_funcion = sp.lambdify(x, funcion)
    evaluar_derivada = sp.lambdify(x, deri)
    
    iters = 0  # Contador de iteraciones
    est_err = 100  # Error inicial

    list_its = []  # Lista para todas las iteraciones
    iter_list = []  # Lista para la iteración actual
        
    if min_error is None:
        min_error = float('inf')
    if max_iters is None:
        max_iters = float('inf')


    while est_err > min_error and iters < max_iters:
        old_x = new_x
        new_x = new_x - (evaluar_funcion(new_x) / evaluar_derivada(new_x))
        est_err = abs((new_x - old_x) / new_x) * 100
        

        iter_list.append([iters, format(new_x, ".3f"), format(est_err,".2f")])
        list_its.append(iter_list.copy())
        
        iters += 1
        iter_list.clear()
    
    return list_its, list_its[-1][1],est_err, new_x


x = sp.Symbol('x')
funcion = sp.sin(x) + sp.cos(1 + x**2) - 1

new_x = 1
min_error = 0.0001
max_iters = None

newton_raphson(new_x, funcion, max_iters, min_error)
