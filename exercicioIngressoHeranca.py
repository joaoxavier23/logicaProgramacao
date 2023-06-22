class Ingresso():
    def __init__(self,valor):
        self.valor=valor

    def imprimeValor(self):
        print(f"O valor do ingresso é {self.valor}")
class IngressoVip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
    def imprimeValor(self):
        print(f"O valor do ingresso vip é {self.valor}")

comprar=Ingresso(5.00)
comprar.imprimeValor()
comprarIngressoVip=IngressoVip(15.00)
comprarIngressoVip.imprimeValor()