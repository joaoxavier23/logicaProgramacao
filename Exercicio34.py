vetorA=[]
contador=0
for x in range(10):
    vetorA.append(int(input("Digite um número: ")))

numero_qualquer=(int(input("Digite outro número: ")))

for y in range(10):
    if numero_qualquer==vetorA[y]:
        contador+=1
        print(vetorA[y],[y])
print("O número",numero_qualquer,"aparece",contador,"Vezes")


