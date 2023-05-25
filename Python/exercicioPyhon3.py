texto = "O rato roeu a roupa do rei de Roma"
def contar_vogais(texto1):
    vogais="aeiouAEIOU"
    num_vogais=0
    for letras in texto1:
        if letras in vogais:
            num_vogais+=1
    return num_vogais
contar_vogais(texto)
print(f"O texto tem {contar_vogais(texto)} vogais.")

