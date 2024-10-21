from sympy import symbols, diff

x = symbols('x')
f = 3*x**2 + 2*x +1

f_prime = diff(f, x)

print(f_prime)