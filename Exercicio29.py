notas=[]
contador=0
soma=0
for x in range(5):
    notas.append(float(input("Digite a nota: ")))
for y in range(5):
    soma+=notas[y]
media=soma/5
for j in range(5):
    if notas[j]>=media:
        contador+=1
print(contador)






