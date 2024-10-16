import pprint

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = (a + b) / 2

est_error = 100 

list_vals = [a, b ,c, est_error] #Primera iteración

new_list = [] #Lista para almacenar valores de las evaluaciones sobre la ecuación

list_its = [] #Lista para almacenar las iteraciones

list_its.append(list_vals) #Insertando la primera iteración

new_itr = 0 #Contador de index para la lista de iteraciones

while est_error > 10:
        
    for value in list_vals[0:3]: #Se itera sobre la lista de primera iteración (a, b, y c)
        
        x = value #Se asigna el valor de la lista a la variable x
        equ = 5 * (x)**3 - 5 * (x)**2 + 6 * (x) - 2 #Se evalua la ecuación para dicho valor
        new_list.append(equ) #Se agrega el valor de la ecuación evaluada en x
              
    if (new_list[0] * new_list[2]) < 0 and (new_list[2] * new_list[1]) > 0:
        
        list_vals = [list_vals[0], list_vals[2]]
        list_vals.append(((list_vals[0] + list_vals[1])/2))
        new_c = list_vals[2] #Se asigna a new_c el valor de c en la nueva iteración 
        old_c = list_its[new_itr][2] #Se asigna a old_c el valor de c en la primera iteración
        est_error = float(format(abs(((new_c - old_c)/(new_c))*100), ".4f")) #Calculo del error estándar
        list_vals.append(est_error) #Se agrega el error estimado a la iteración
        list_its.append(list_vals) #Se agrega la nueva iteración a la lista de iteraciones
        new_list.clear() #Se vacía la lista nueva
        new_itr += 1  #Se suma 1 al valor actual del contador de la lista de iteraciones
        
    elif (new_list[0] * new_list[2]) > 0 and (new_list[2] * new_list[1]) < 0:
        
        list_vals = [list_vals[2], list_vals[1]]
        list_vals.append(((list_vals[0] + list_vals[1])/2))
        new_c = list_vals[2] #Se asigna a new_c el valor de c en la nueva iteración 
        old_c = list_its[new_itr][2] #Se asigna a old_c el valor de c en la primera iteración
        est_error = float(format(abs(((new_c - old_c)/(new_c))*100), ".4f")) #Calculo del error estándar
        list_vals.append(est_error) #Se agrega el error estimado a la iteración
        list_its.append(list_vals) #Se agrega la nueva iteración a la lista de iteraciones
        new_list.clear() #Se vacía la lista nueva
        new_itr = new_itr + 1  #Se suma 1 al valor actual del contador de la lista de iteraciones

print(f"El número de iteraciones realizadas para obtener un error menor a 10% fue de: {len(list_its)}")
pprint.pprint(list_its)