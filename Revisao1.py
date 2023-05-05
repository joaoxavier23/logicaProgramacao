continuar="S"
mediaArray=[]
while continuar=="S":
    nota1= int(input("Digite a primeira nota: "))
    nota2= int(input("Digite a segunda nota: "))
    media= nota1+nota2
    media=media/2
    mediaArray.append(media)
    print("Media foi:",media)
    if media>=7:
        print("Aluno aprovado")
    elif media>=4:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")
    continuar = input("Digite S para continuar N para sair: ")
print(mediaArray)