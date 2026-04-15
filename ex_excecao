class ValorInvalido(Exception): #personalizando uma exceção
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)# sobrecarregando o construtor da classe mãe
        

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    @property #getter
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
        
    @property #getter
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, valor):
        if not isinstance(valor, float) or valor <= 0:# not isinstance(valor, float) validando o tipo
            raise ValorInvalido("Valor inválido") #levantamento de exceção
        self.__preco = valor
try:        
    p1 = Produto("teclado", 350)
    p2 = Produto("monitor", 8000)
    p3 = Produto("mouse", -100)
    p4 = Produto("mouse", "-100")
except ValorInvalido as e:
    print(f"Erro {e}")
