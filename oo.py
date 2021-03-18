#relembrando como criar classes e objetos

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo,self.titular))

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor




conta = Conta(123,"leo",60.0,1000.0)

conta.depositar(40)

conta.sacar(20)

conta.extrato()
