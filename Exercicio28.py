alunosSala= int(input("Quantos alunos tem na sala? "))
listaAluno=[]
for x in range (alunosSala):
    listaAluno.append(input("Digite o nome do aluno: "))
for i in range(alunosSala):
    print(listaAluno[i],i)