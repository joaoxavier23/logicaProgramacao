maca = int(input("Digite a quantidade de maças para comprar: "))

if maca<12:
    macaPreco=1.30
    maca= maca*macaPreco
    print("Valor da compra:",maca)
else:
    macaPreco=1.00
    maca=maca*macaPreco
    print("Valor da compra:",maca)
