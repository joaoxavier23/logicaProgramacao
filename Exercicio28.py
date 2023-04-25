quantidadeAlunos= int(input("Quantos alunos tem na sala? "))
listaAlunos=[]
for x in range (quantidadeAlunos):
    listaAlunos.append(input("Digite o nome do aluno: "))
#for i in range(quantidadeAlunos):
    #print(listaAlunos[i], i)
checarNome= input("Digite um nome para checar se está na lista: ")

for y in range(quantidadeAlunos):
    if checarNome==listaAlunos[y]:
        print(y, listaAlunos[y])





