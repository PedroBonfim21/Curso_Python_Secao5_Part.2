salarioAt=float(input("Digite seu salario atual:\n"))
tempoServ=float(input("Digite seu tempo de trabalho na empresa(anos):\n"))
if salarioAt<=500:
   salarioAt=salarioAt*1.25
elif salarioAt<= 1000:
   salarioAt=salarioAt*1.20
elif salarioAt<=1500:
   salarioAt=salarioAt*1.15
elif salarioAt<=2000:
   salarioAt=salarioAt*1.10

if tempoServ==1 or tempoServ<=3:
    salarioAt=salarioAt+100
elif 3< tempoServ<7:
    salarioAt=salarioAt+200
elif 6 < tempoServ < 11:
    salarioAt=salarioAt+300
elif tempoServ>10:
    salarioAt=salarioAt+500
print(f"O seu salario atual é de {salarioAt}")
