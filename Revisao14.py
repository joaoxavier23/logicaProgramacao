inicioJogo = int(input("Digite a hora de inicio do jogo: "))
terminoJogo = int(input("Digite a hora do termino do jogo: "))
if inicioJogo<terminoJogo:
    print(terminoJogo-inicioJogo)
else:print(24-inicioJogo+terminoJogo)
