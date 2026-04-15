'''
Atividade 1 – Soma de números personalizados


Crie uma classe Numero com:

atributo valor
sobrecarga do operador +

O resultado deve ser a soma dos valores

'''

class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro):
        return self.valor + outro.valor

      
n1 = Numero(3)
n2 = Numero(4)
n3 = Numero(20)

print(n1 + n2)
