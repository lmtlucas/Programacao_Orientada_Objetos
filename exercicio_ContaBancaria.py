class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def ver_saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")
    
    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)


c1 = ContaBancaria("Jose", 15820)
c2 = ContaBancaria("Maria", 84623)

print(c1.ver_saldo())

c1.depositar(100)

print(c1.ver_saldo())

c1.sacar(500555555)
c1.sacar(500)

print(c1.ver_saldo())
print(c2.ver_saldo())

c1.transferir(1000,c2)

print(c1.ver_saldo())
print(c2.ver_saldo())


