# Programação Orientada a Objetos

## Os principais conceitos:
- Classes
- Objetos
- Encapsulamento
- Herança
- Polimorfismo

### Classes:
Uma classe é um modelo (molde) para criar objetos
Ela define:
- Atributo: são os dados do objeto (características)
- Métodos: Funções dentro da classe (ações)

Ex.:
````
class Pessoa:
  def __init__(self, nome, idade): # __init__ é o método construtor usado para definir os atributos
    self.nome = nome # atributo
    self.idade = idade # atributo
  def falar(self): #métodos/funções
    print("Olá")

````
### Objetos:
São instâncias de uma classe

Ex.:
```
p1 = Pessoa("joão", 20)
p2 = Pessoa("Maria",26)
```
### Encapsulamento:
Encapsulamento é proteger os dados da classe. Controlando o acesso usando métodos.

Tipos de aceso:
- publico (sem underline)
- _protegido (um underline
- __privado (duplo underline)

Ex.:
```
class conta:
  def __init__(self, saldo): 
    self._saldo = saldo # _ protegido
```

### Herança:
Encapsulamento é proteger os dados da classe. Contr
