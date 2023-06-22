nomes=[]
senhas=[]
for x in range(2):
    nomes.append(input("Digite seu nome: "))
    senhas.append(input("Digite sua senha: "))
nomelogin= input("Usuario para login: ")
senhalogin= input("Senha para login")

for y in range(2):
    if nomes[y]==nomelogin and senhas[y]==senhalogin:
        print(nomes[y],"Login efetuado com sucesso")

