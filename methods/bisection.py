from pprint import pprint

def metodo_biseccion(a, b, funcion, error_minimo=10, max_iteraciones=1000):
    
    def evaluar_funcion(x):
        
        return eval(funcion)
    
    c = (a + b) / 2
    est_error = 100 
    list_vals = [a, b, c, est_error]
    list_its = [list_vals]
    new_itr = 0
    
    while est_error > error_minimo and new_itr < max_iteraciones:
        
        new_list = [evaluar_funcion(x) for x in list_vals[:3]]
        
        if (new_list[0] * new_list[2]) < 0:
            list_vals = [list_vals[0], list_vals[2]]
        elif (new_list[0] * new_list[2]) > 0:
            list_vals = [list_vals[2], list_vals[1]]
        else:
            break
        
        list_vals.append((list_vals[0] + list_vals[1]) / 2)
        new_c = list_vals[2]
        old_c = list_its[new_itr][2]
        est_error = abs((new_c - old_c) / new_c) * 100
        list_vals.append(format(est_error, ".2f"))
        list_its.append(list_vals)
        new_itr += 1
    
    return new_itr + 1, list_vals[2], est_error, list_its

a = 0
b = 1
funcion = "5 * x**3 - 5 * x**2 + 6 * x - 2"
max_iteraciones = 5

iteraciones, raiz, error_final, lista_iteraciones = metodo_biseccion(a, b, funcion, max_iteraciones = 5)

print(f"Número de iteraciones: {iteraciones}")
print(f"Raíz encontrada: {raiz}")
print(f"Error final: {error_final}%")
print("\nLista de iteraciones:")
pprint(lista_iteraciones)