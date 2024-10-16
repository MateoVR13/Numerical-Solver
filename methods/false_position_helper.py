import math

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

# f_a = 5 * (a)**3 - 5 * (a)**2 + 6 * (a) - 2
# f_b = 5 * (b)**3 - 5 * (b)**2 + 6 * (b) - 2

f_a = 7 * math.sin(a) * math.exp(-a) - 1
f_b = 7 * math.sin(b) * math.exp(-b) - 1

c = b - ((f_b)*(a-b)/(f_a - f_b))

# f_c = 5 * (c)**3 - 5 * (c)**2 + 6 * (c) - 2

f_c = 7 * math.sin(c) * math.exp(-c) - 1

print(f"El valor de a es {a}")
print(f"El valor de b es {b}")
print(f"El valor de c es {c}")
print(f"El valor de fa es {f_a}")
print(f"El valor de fb es {f_b}")
print(f"El valor de fc es {format(f_c, ".4f")}")

if (f_a * f_c)<0:
    print("f(a)*f(c) = -")
else:
    print("f(a)*f(c) = +")