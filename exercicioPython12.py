class ContaBancaria:
    def __init__(self,numero_conta,saldo,nome_cliente,tipo_conta):
        self.numero_conta=numero_conta
        self.saldo=0
        self.status_conta=True
        self.nome_cliente=nome_cliente
        self.tipo_conta=tipo_conta
        self.limite_credito=50
        self.limite_disponivel=self.limite_credito

    def depositar(self,deposito):
        if self.status_conta==True:
            self.deposito = deposito
            self.saldo= self.saldo+deposito

            print(f"{self.nome_cliente} depositou {self.deposito}")
        else:
            print("Não foi possivel realizar o deposito, conta desativada.")
    def sacar(self,saque):
        if self.status_conta==True and self.saldo >= saque:
            self.saque=saque
            self.saldo=self.saldo - saque
            print(f"{self.nome_cliente} sacou {self.saque}")
        elif self.status_conta==True and self.saldo >=saque or self.saldo + self.limite_disponivel >=saque:
            self.saque=saque
            self.saldo = self.saldo + self.limite_disponivel
            self.saldo = self.saldo - saque
            self.limite_disponivel = 0


            print(f"{self.nome_cliente} sacou {self.saque} seu saldo é {self.saldo} e seu limite {self.limite_disponivel}")
        else:
            print("Saque indisponivel")
    def verificarSaldo(self):
        if self.status_conta==True:
            print(f"O seu saldo é {self.saldo}")
    def desativarConta(self):
        if self.saldo == 0 and self.status_conta==True:
            self.status_conta=False
            print("Conta desativada com sucesso!")
        elif self.status_conta==False:
            print("Conta já desativada")
        else:
            print("Não foi possivel desativar a conta, certifique-se que o seu saldo esteja zerado")
    def ativarConta(self):
        if self.status_conta==False:
            self.status_conta=True
            print("Conta ativada com sucesso")
        else:
            print("Sua conta já está ativada")
    def ativarLimite(self):
        if self.limite_credito > 0:
            self.limite_credito = 50
            print(f"Seu limite de credito é {self.limite_credito}")
    def desativarLimite(self):
        if self.limite_disponivel==0:
            self.limite_credito=0
            print(f"Seu limite de credito foi desativado")
        else:
            print(f"Seu limite de crédito é {self.limite_disponivel} não foi possivel desativar")



p1= ContaBancaria(10,1500,"João","Corrente")
print(vars(p1))
p1.verificarSaldo()
p1.depositar(1500)
p1.verificarSaldo()
p1.depositar(1500)
p1.verificarSaldo()
p1.ativarLimite()
p1.sacar(3020)
p1.verificarSaldo()
p1.desativarLimite()
p1.depositar(100)
p1.verificarSaldo()
print(vars(p1))