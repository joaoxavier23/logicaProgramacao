while True:
    numero1 = int(input("Digite um número maior que 0: "))
    while numero1 == 0:
        numero1 = int(input("Digite um número maior que 0: "))
    if numero1>0:
        print("Número positivo")
    elif numero1<=-1:
        print("Número negativo")
    continuar = input("Digite S para continuar ou N para sair: ")
    if continuar=="N" or continuar=="n":
        break


