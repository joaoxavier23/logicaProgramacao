while True:
    menu = int(input("1 Somar/2 Subtrair/3 Multiplicar/4 Dividir/5 Sair: "))
    def soma(numero1,numero2):
        return numero1 + numero2
    def subtrai(numero1,numero2):
        return numero1 - numero2
    def multiplica(numero1,numero2):
        return numero1 * numero2
    def divide(numero1,numero2):
        return numero1 / numero2

    match menu:
        case 1:
            numero1 = int(input("Digite o primmeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            print(soma(numero1,numero2))
        case 2:
            numero1 = int(input("Digite o primmeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            print(subtrai(numero1,numero2))

        case 3:
            numero1 = int(input("Digite o primmeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            print(multiplica(numero1,numero2))

        case 4:
            numero1 = int(input("Digite o primmeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            print(divide(numero1,numero2))

        case 5:
            break
        case _:
            print("Opção inválida")


