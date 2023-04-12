contador = 1
soma = 0
quantidadeAlunos = int(input("Digite a quantidade de alunos: "))
while contador<=quantidadeAlunos:
    notaAluno = int(input("Digite a nota do aluno: "))
    soma = soma + notaAluno
    contador= contador +1
media= soma/quantidadeAlunos
print(media)

