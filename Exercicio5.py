litros=int(input("Digite quantos litros você vai abastecer: "))
combustivel=input("Digite G para gasolina e E para etanol: ")

if combustivel=="G" or combustivel=="E":
   if combustivel=="G":
      print("Litros:",litros,"\nGasolina valor total:",litros*5.80)
   else:
       combustivel=="E"
       print("Litros:",litros,"\nEtanol valor total:",litros*4.90)

else:
    print("Digite o tipo de combustivel correto")
