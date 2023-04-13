contador = 0
contador2 = 0
for x in range(10):
    numero= int(input("Digite um número: "))
    if numero>=10 and numero<=20:
        contador=contador+1
    else:
        contador2=contador2+1
print("Numeros entre 10 e 20: ",contador,"\nNumeros menores que 10 e maiores que 20: ",contador2)