time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")
golsTime1 = int(input("Digite a quantidade de gols do primeiro time: "))
golsTime2 = int(input("Digite a quantidade de gols do segundo time: "))

if golsTime1!=golsTime2:
   if golsTime1>golsTime2:
       print("O vencedor foi o time: ",time1)
   else:
       print("O vencedor foi o time: ",time2)

else:
    print("Empate")