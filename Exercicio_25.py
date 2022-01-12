from math import sqrt
a = float(input("informe o valor de A : "))
b = float(input("informe o valor de B : "))
c = float(input("informe o valor de C : "))
delta = (b**2)-(4*a*c)
if delta<0:
    print("Não existe raiz")
elif delta==0:
    raizdelta = (-1 * b +(sqrt(delta))/(2*a))
    print(delta)
elif delta>=0:
    x1 = (-1 * b + sqrt(delta)) / (2 * a)
    x2 = (-1 * b - sqrt(delta) / (2 * a))
    print(f"As duas raizes são: {x1} e {x2} ")