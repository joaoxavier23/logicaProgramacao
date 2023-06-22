while True:
    numero1 = int(input("Digite o primeiro valor: "))
    numero2 = int(input("Digite o segundo valor: "))

    while numero1==numero2:
        numero2 = int(input("O segundo valor não pode ser igual ao primeiro, digite novamente: "))

    if  numero1>numero2:
        print(numero2,numero1)
    else:print(numero1,numero2)
    continuar=input("Deseja continuar? S/N: ")
    if continuar=="N" or continuar=="n":
        print("Fim do programa!")
        break