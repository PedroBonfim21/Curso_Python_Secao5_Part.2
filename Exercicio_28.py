from numpy import cbrt
x=int(input("Digite o x: "))
y=int(input("Digite o y: "))
z=int(input("Digite o z: "))
Media=int(input("Escolha o tipo de media que será calculada:\n(1)-Geométrica\n(2)-Ponderada\n(3)-Harmônica\n(4)-Aritmética\nDigite o número da média desejada(1,2,3,4):\n"))
if Media==1:
    Geometrica=cbrt((x*y*z))
    print(f"O resultado da média geometrica entre os números é: {Geometrica} .")
elif Media==2:
    Ponderada=(x+(2*y)+(3*z))/6
    print(f"O resultado da média ponderada entre os números é: {Ponderada} .")
elif Media==3:
    Harmônica=1/((1/x)+(1/y)+(1/z))
    print(f"O resultado da média harmônica entre os números é: {Harmônica} .")
elif Media==4:
    Aritmética=(x+y+z)/3
    print(f"O resultado da média aritmética entre os números é: {Aritmética} .")
    