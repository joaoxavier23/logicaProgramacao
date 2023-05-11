A = []
contador=0
numeros=0
while True:
    if numeros %2!=0:
        A.append(numeros)
        contador+=1
    numeros+=1
    if contador==10:
        break
print(A)
