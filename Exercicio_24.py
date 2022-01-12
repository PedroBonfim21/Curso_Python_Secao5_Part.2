prod=float(input("Digite o valor do produto: "))
est=int(input("Digite 1 para MG \n""Digite 2 para SP \n""Digite 3 para RJ \n""Digite 4 para MS \n"))
if est==1:
    est=prod * 1.07
elif est==2:
    est=prod * 1.12
elif est==3:
    est=prod * 1.15
else:
    est=prod*1.08
print(f"O valor do produto acrescido do imposto Estadual é: R${est:.2f}")
