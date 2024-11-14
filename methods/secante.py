import sympy as sp

def metodo_secante(x0, x1, funcion, max_iters=None, min_error=None):
    x = sp.Symbol('x')

    def evaluar_funcion(x):
        return eval(funcion)
    
    iters = 0
    est_err = 100
    list_its = [[iters, x0, x1, est_err]]
    
    while True:
        old_x1 = x1
        x1 = x1 - evaluar_funcion(x1) * (x1 - x0) / (evaluar_funcion(x1) - evaluar_funcion(x0))
        est_err = abs((x1 - old_x1) / x1) * 100
        
        iters += 1
        list_its.append([iters, x0, old_x1, est_err])
        
        if min_error is not None and est_err < min_error:
            break
        
        if max_iters is not None and iters >= max_iters:
            break
        
        x0 = old_x1
        
    return list_its, est_err, x1
