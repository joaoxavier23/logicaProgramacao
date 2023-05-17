lista_produtos=[]
preco_produtos=[]
def somar(numero1, numero2):
    return numero1 + numero2
def subtrair(numero1, numero2):
    return numero1 - numero2
def multiplicar(numero1, numero2):
    return numero1 * numero2
def dividir(numero1, numero2):
    return numero1 / numero2
def retornar_positivo(numero1):
    if numero1>0:
        return "P"
    else:
        return "Z"
def adicionar_produto_preco(a,b):
    lista_produtos.append(a)
    preco_produtos.append(b)
def somarTodos(*a):
    contador=0
    for x in a:
        contador += x
    return contador
def texto(texto1):
    contador=0
    texto_def = ""
    for x in texto1:
        if x not in " ":
            contador+=1
    for i in range(contador):
        texto_def=texto1

    return contador,texto_def,texto_def[::-1]
nova_lista=[]
a=[1,2,2,3,4,4,5,3,6,7,8]
def lista(l):
    for x in a:
        if x not in nova_lista:
            nova_lista.append(x)
    return a,nova_lista
def num_primo(a):
    for x in range(3,a):
        if a%x ==0:
            return f"O numero {a} não é primo"
    if a ==1:
            return f"O numero {a} não é primo"
    if a ==2:
            return f"O numero {a} é primo"
    return f"O numero {a} é primo"



