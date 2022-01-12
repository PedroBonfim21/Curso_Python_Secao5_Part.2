chegada = str(input("Digite a hora de chegada:\nEx:18:30 \n"))
saida = str(input("Digite a hora de saida:\nEx:18:40 \n"))

hora, minu = chegada.split(":")
sHor, sMinu = saida.split(":")

hora = int(hora)
minu = int(minu)
sHor = int(sHor)
sMinu = int(sMinu)
temM = 0
temH = 0

if hora < sHor:
    temH = (sHor - hora)
    if minu < sMinu:
        temH = temH + 1

elif hora > sHor:
    temH = 24 - (hora - sHor)
    if minu < sMinu:
        temH = temH + 1

elif hora == sHor and minu > sMinu:
    temH = 24

elif hora == sHor and minu == sMinu:
    temH = 1

elif hora == sHor and minu < sMinu:
    temH = 1

if temH < 3:
    print(f"O valor cobrador será de R${temH * 1  :.2f}")
elif temH==3 or temH==4:
   print(f"O valor cobrador será de R${2+((temH - 2)*1.4):.2f}")
else:
    print(f"O valor cobrador será de R${(2+2.4)+((temH - 4)*2):.2f}")
