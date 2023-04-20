operacao = 5
while operacao!=6:
    numero1=float(input("Digite o primeiro número: "))
    numero2=float(input("Digite o segundo número: "))

    while True:
        operacao = int(input("Digite 1 para soma\nDigite 2 para subtração\nDigite 3 para multiplicação\nDigite 4 para divisão\nDigite 5 para digitar novo número\nDigite 6 para sair:"))
        match operacao:
            case(1):
               resultado= numero1+numero2
               print(resultado)
               break

            case(2):
                resultado= numero1-numero2
                print(resultado)
                break

            case(3):
                resultado= numero1*numero2
                print(resultado)
                break

            case(4):
                resultado= numero1/numero2
                print(resultado)
                break
            case(5):
                break
            case(6):
                break

