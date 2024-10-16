new_c = float(input("Ingrese el valor del nuevo c: "))
old_c = float(input("Ingrese el valor del anterior c: "))

est_error = abs((new_c - old_c)/(new_c))*100

print(f"El error estimado es: {est_error}")