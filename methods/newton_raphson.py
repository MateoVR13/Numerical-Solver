import numpy as np
import sympy as sp
import math

def newton_raphson(new_x, funcion, max_iters = None, min_error = None):
    
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
