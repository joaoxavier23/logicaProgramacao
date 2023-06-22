doidera=[]
contador=0
contador2=0
soma=0
for x in range(10):
    doidera.append(int(input("Digite um número: ")))
    soma+=doidera[x]
media=soma/10
maior = doidera[0]
menor = doidera[0]
#Numeros acima da media
for j in range(10):
    if doidera[j]>media:
        contador2+=1
#Numeros pares
for y in range(10):
    if doidera[y] %2 == 0:
        contador+=1
#Menor e maior valor existente
for doidera in doidera:
    if doidera > maior:
        maior=doidera
    elif doidera<menor:
        menor=doidera
print("Existem",contador,"Números pares")
print("Maior numero",maior,"Menor numero",menor)
print(contador2,"Números acima da média")
