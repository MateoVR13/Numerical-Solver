import numpy as np

def metodo_trapecio(funcion, a, b, n):
    def f(x):
        return eval(funcion)
    
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = [f(xi) for xi in x]
    
    integral = h * (y[0]/2 + sum(y[1:-1]) + y[-1]/2)
    
    # Create interval data table
    intervals = [[i, float(x[i]), float(y[i])] for i in range(len(x))]
    
    return integral, intervals