class Animal:
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"O animal {self.nome} está comendo")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def emitirSom(self):
        print(f"O {self.nome} saiu miando")
    def comer(self,comida):
        print(f"O {self.nome} está comendo {comida}")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def emitirSom(self):
        print(f"O {self.nome} saiu latindo")
    def comer(self,comida):
        print(f"O {self.nome} está comendo {comida}")

animal1=Gato("Kliw","Cinza")
animal1.emitirSom()
animal1.comer("ração")
animal2=Cachorro("Spike","Amarelo")
animal2.emitirSom()
animal2.comer("Osso")