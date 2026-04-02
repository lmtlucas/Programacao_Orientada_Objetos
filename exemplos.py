#class Pessoa  a primeira letra da classe em maiusculo
#self declarar atributo
# class representação do objeto
# init utilizado para iniciarlizar os valores das variaveis p
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print("Olá sou o",self.nome)

p1 = Pessoa("João", 20)
p2 = Pessoa("Maria", 25)

print(f"Nome: {p1.nome} nome:{p1.idade}")

p1.falar()

class Conta:
    def __init__(self, saldo):
        self.__saldo = saldo

    def saldo_atual(self):
        return self.__saldo
    def adicionar_valor(self,valor):
        self.__saldo += valor
    def debitar(self, valor):
        if valor > self.__saldo:
            print("saldo insuficiente")
        else:
            self.__saldo -= valor
            print(f"Valor R$ {valor} debitado")

c1 = Conta(1520)

c1.adicionar_valor(652)
c1.debitar(520321)
print(c1.saldo_atual())
c1.debitar(253)
