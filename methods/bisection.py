import numpy as np
import sympy as sp
import math

def metodo_biseccion(a, b, funcion, error_minimo = None, max_iteraciones = None):
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
