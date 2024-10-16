import math

#new_x = 0
# new_x = -1.5
#new_x = 3
# new_x = 3
# new_x = 0.5
new_x = 1
iters = 0

est_err = 100

while est_err > 0.0001 :
    
    # func = math.exp(-new_x) - new_x
    # deri = -math.exp(-new_x) - 1
    # func = new_x**3 - 2*new_x + 1
    # deri = 3*new_x**2 - 2
    # func = new_x**5 - new_x - 1 
    # deri = 5*new_x**4 - 1
    # func = 2*new_x**3 - 11.7*new_x**2 + 17.7*new_x - 5 
    # deri = 6*new_x**2 - 23.4*new_x + 17.7
    # func = math.sin(math.sqrt(new_x)) - new_x 
    # deri = math.cos(math.sqrt(new_x)) * (1/(2*math.sqrt(new_x))) - 1
    func = math.sin(new_x) + math.cos(1 + new_x**2) - 1
    deri = math.cos(new_x) - math.sin(1 + new_x**2)*2*new_x
    print(f"| Iteración {iters} | Xi = {format(new_x, ".3f")} | Ea% = {format(est_err, ".3f")} |")
    old_x = new_x
    new_x = new_x-(func/deri)
    est_err = abs((new_x - old_x)/(new_x))*100
    iters += 1