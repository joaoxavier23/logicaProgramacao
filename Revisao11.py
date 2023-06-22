total_eleitores=int(input("Digite o total de eleitores: "))
votos_brancos=int(input("Digite o total de votos brancos: "))
votos_nulos=int(input("Digite o total de votos nulos: "))
votos_validos=int(input("Digite o total de votos validos: "))

somaVotos_brancos= (votos_brancos/total_eleitores)*100
somaVotos_nulos= (votos_nulos/total_eleitores)*100
somaVotos_validos= (votos_validos/total_eleitores)*100

print("Total de votos brancos ",somaVotos_brancos,"%","\nTotal de votos nulos ",somaVotos_nulos,"%"
      ,"\nTotal de votos válidos ",somaVotos_validos,"%")