numeros = []
for x in range(3):
    numeros.append(int(input("Digite um número: ")))
maior = numeros[0]
menor = numeros[0]
for numeros in numeros:
    if numeros>maior:
        maior=numeros
        print("Maior:",maior)
    elif numeros<menor:
        menor=numeros
        print("Menor:",menor)


