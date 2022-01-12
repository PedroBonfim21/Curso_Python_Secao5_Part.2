km=float(input("Digite a quantidade de Km: "))
litros=float(input("Digite a quantidade de litros consumidos pelo carro: "))
Km_L=km/litros
if Km_L<8:
    print("Venda o carro")
elif Km_L>=8 or Km_L<=12:
    print("Econômico")
elif Km_L>12:
    print("Super econômico")
