class Pessoa:
    def __init__(self,nome,peso,idade,comendo=False,falando=False,andando=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
        self.falando=falando
        self.andando=andando
    def comer(self,comida):
        self.comida = comida
        if self.comendo == False:
            print(f"{self.nome} está comendo {self.comida}")
            self.comendo=True
        elif self.falando==True:
            print(f"{self.nome} não pode comer pois esta falando")

        else:
            print(f"{self.nome} já está comendo.")
    def pararcomer(self):
        if self.comendo == True and self.falando==False:
            print(f"{self.nome} parou de comer.")
            self.comendo=False
        else:
            print(f"{self.nome} não está comendo.")
    def falar(self,fala):
        self.fala=fala
        if self.comendo == False and self.falando == False:
            print(f"{self.nome} disse {self.fala}")
            self.falando=True
        elif self.falando == True:
            print(f"{self.nome} já está falando algo")
        else:
            print(f"{self.nome} não pode falar por que está comendo.")
    def parardefalar(self):
        if self.falando==True:
            print(f"{self.nome} parou de falar")
            self.falando=False
        else:
            print(f"{self.nome} não está falando")
    def andar(self):
        print(f"{self.nome} está andando")
        self.andando=True
    def parardeandar(self):
        if self.andando==True:
            print(f"{self.nome} parou de andar")
            self.andando==False
        else:
            print(f"{self.nome} não está andando")

p1= Pessoa("João",80,19)
print(vars(p1))
p1.comer("pipoca")
p1.comer("Mamão")
p1.parardeandar()
p1.pararcomer()
p1.parardefalar()
p1.comer("Banana")
p1.falar("oi")
p1.pararcomer()
p1.falar("oi")
p1.falar("beleza")
p1.parardefalar()
p1.andar()
#p2= Pessoa("Maria",56,22,comendo=True)
#print(vars(p2))
