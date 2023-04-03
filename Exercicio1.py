nome= input("Digite um nome: ")
idade= int(input("Digite sua idade: "))
salario= float(input("Digite o seu salário: "))
percentualAumento= int(input("Digite quantos % foi seu aumento esse mês: "))

salarioSoma= (salario*percentualAumento)/100
totalSalario=(salario+salarioSoma)
print(nome, "Tem",idade," Anos de idade e recebe ",totalSalario," Por mês")