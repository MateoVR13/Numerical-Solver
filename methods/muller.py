import sympy as sp


def metodo_muller(x0, x1, x2, funcion, max_iters=None, min_error=None):
    x = sp.Symbol('x')
    
    def evaluar_funcion(x):
        return eval(funcion)
    
    iters = 0
    est_err = 100
    list_its = [[iters, x0, x1, x2, est_err]]
    
    while True:
        h1, h2 = x1 - x0, x2 - x1
        d1 = (evaluar_funcion(x1) - evaluar_funcion(x0)) / h1
        d2 = (evaluar_funcion(x2) - evaluar_funcion(x1)) / h2
        a = (d2 - d1) / (h2 + h1)
        b = a * h2 + d2
        c = evaluar_funcion(x2)
        
        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            raise ValueError("El método de Muller requiere raíces reales en cada paso.")
        
        sqrt_disc = discriminant**0.5
        x3 = x2 + (-2 * c) / (b + sqrt_disc if b > 0 else b - sqrt_disc)
        est_err = abs((x3 - x2) / x3) * 100
        
        iters += 1
        list_its.append([iters, x0, x1, x2, est_err])
        
        if min_error is not None and est_err < min_error:
            break
        
        if max_iters is not None and iters >= max_iters:
            break
        
        x0, x1, x2 = x1, x2, x3
        
    return list_its, est_err, x3
