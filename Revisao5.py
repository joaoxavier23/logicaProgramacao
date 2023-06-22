numero = int(input("Digite um número: "))

if numero %2==0:
    if numero<=-1:
        print("Número par negativo")
    elif numero>=0:
        print("Número par positivo")
else:
    if numero<=-1:
        print("Número impar negativo")
    elif numero>=0:
        print("Número impar positivo")
