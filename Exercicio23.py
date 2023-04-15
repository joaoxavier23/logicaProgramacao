nota1=float(input("Digite a nota do aluno: "))
while nota1<0 or nota1>10:
   nota1= float(input("Digite a primeira nota válida: "))
nota2=float(input("Digite a segunda nota do aluno: "))
while nota2<0 or nota2>10:
   nota2= float(input("Digite a segunda nota válida: "))
media=(nota1+nota2)/2
print("A média foi:",media)

continuar = input("Deseja continuar? digite s se sim: ")
while continuar=="s":
    nota1 = float(input("Digite a nota do aluno: "))
    while nota1 < 0 or nota1 > 10:
      nota1 = float(input("Digite a primeira nota válida: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    while nota2 < 0 or nota2 > 10:
       nota2 = float(input("Digite a segunda nota válida: "))
    media = (nota1 + nota2) / 2
    print("A média foi:", media)
    continuar = input("Deseja continuar? digite S se sim: ")
else:print("Fim do programa!")
