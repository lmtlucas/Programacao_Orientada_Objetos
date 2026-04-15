'''
Sobregarga de operadores

+      __add__
-      __sub__
*      __mul__
/      __truediv__
==     __eq__
<      __lt__
>      __gt__
str()  __str__


'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __add__(self, outro):
        return self.preco + outro.preco
    def __eq__(self, outro):
        return self.preco == outro.preco
    def __str__(self):
        return f"Nome do produto: {self.nome} e valor: {self.preco}"
      
p1 = Produto("teclado", 350)
p2 = Produto("monitor", 8000)
p3 = Produto("mouse", 100)

print(p1 + p2)
print(p1 == p2)
print (p3)


class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y) # a soma cria um novo objeto Vetor
    def __str__(self):
        return f"({self.x}, {self.y})"
        
v1 = Vetor(2, 6)
v2 = Vetor(3, 8)
print(v1+v2) # print do novo objeto Vetor

