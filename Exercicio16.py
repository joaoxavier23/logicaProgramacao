total = 0
for x in range(0,10):
    numero = int(input("Digite um numéro: "))
    if numero<0:
        total=total+1
print("Números negativos: ",total)