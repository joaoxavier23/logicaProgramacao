while True:
    resposta = int(input("Digite 1 para Área para triangulo/2 Área retangulo/3 encerrar: "))
    match resposta:
        case 1:
            baseTriangulo=float(input("Digite a base: "))
            alturaTriangulo=float(input("Digite a altura: "))

            areaTriangulo=(baseTriangulo*alturaTriangulo)/2
            print("Área triangulo",areaTriangulo)
        case 2:
            baseRetangulo=float(input("Digite a base: "))
            alturaRetangulo=float(input("Digite a altura: "))

            areaRetangulo=(baseRetangulo*alturaRetangulo)
            print("Área retangulo",areaRetangulo)
        case 3:
            break
        case _:
            print("Valor inválido")

    # if resposta==1:
    #     baseTriangulo= float(input("Digite o valor da base: "))
    #     alturaTriangulo= float(input("Digite o valor da altura: "))
    #
    #     area=(baseTriangulo*alturaTriangulo)/2
    #     print("Área",area)
    #     resposta=input("1 Área para triangulo/2 Área retangulo/3 encerrar: ")
    # if resposta==2:
    #     baseRetangulo=float(input("Digite o valor da base:"))
    #     alturaRetangulo=float(input("Digite o valor da altura"))
    #
    #     areaRetangulo=(baseRetangulo*alturaRetangulo)
    #     print("Área retangulo",areaRetangulo)
    # if resposta==3:
    #     break
    # if resposta!=1 and resposta!=2 and resposta!=3:
    #     print("Valor inválido")
