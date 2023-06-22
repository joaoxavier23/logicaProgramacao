contador=0
senhaCadastro=int(input("Digite sua senha de cadastro: "))
senhaEntrar=int(input("Digite sua senha: "))
if senhaEntrar!=senhaCadastro:
    while contador<3:
        senhaEntrar = int(input("Senha errada digite novamente: "))
        contador+=1
        if senhaEntrar==senhaCadastro:
            print("Bem vindo!")
            break
elif senhaEntrar==senhaCadastro:
    print("Bem vindo!")
if senhaEntrar!=senhaCadastro and contador==3:
    print("Senha bloqueada!")
