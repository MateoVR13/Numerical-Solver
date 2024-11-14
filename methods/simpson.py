import numpy as np

def metodo_simpson(funcion, a, b, n):
    if n % 2 != 0:
        raise ValueError("n debe ser par")
    
    def f(x):
        return eval(funcion)
    
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = [f(xi) for xi in x]
    
    integral = h/3 * (y[0] + y[-1] + 
                     4*sum(y[i] for i in range(1, n, 2)) +
                     2*sum(y[i] for i in range(2, n-1, 2)))
    
    # Create interval data table
    intervals = [[i, float(x[i]), float(y[i])] for i in range(len(x))]
    
    return integral, intervals
