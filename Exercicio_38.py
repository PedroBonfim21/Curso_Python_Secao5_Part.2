nascimento=input("Digite a data de nascimento(DD/MM/AAAA): ")
dia,mes,ano= nascimento.split("/")
dia= int (dia)
mes= int (mes)
ano= int (ano)
valida=False
if 0>mes<13:
    print("Mês invalido")
else:
    if mes==2:
        if ano%400==0 or ano%4==0 or ano%100 !=0:
           if dia<=29:
               valida=True
               if dia>=30:
                   valida=False
        elif dia<=28:
            valida=True
    elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        if 1<=dia<=31:
            valida=True
            if 1>dia>=32:
                valida=False
    elif mes==4 or mes==6 or mes==9 or mes==11:
        if 1<=dia<=30:
            valida=True
            if 1>dia>=31:
                valida=False
if valida==False:
    print("Dia incorreto")
if ano<=2022:
    if valida==True:
        print("A data é valida")
elif ano <=2022:
    print("Ano incorreto")

