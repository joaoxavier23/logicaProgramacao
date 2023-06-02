from funcoes import *

while True:
    produto=int(input("Digite o nome do produto: "))
    preco=float(input("Digite o preço do produto: "))
    adicionar_produto_preco(produto,preco)
    continuar=input("Deseja continnuar? s/n: ")
    if continuar == "N" or continuar == "n":
        break
print("Produtos: ",lista_produtos)
print("Preços: ",preco_produtos)