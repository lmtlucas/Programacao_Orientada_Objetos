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
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
````
### Objetos:
São instâncias de uma classe

Ex.:
```
p1 = Pessoa("joão", 20)
p2 = Pessoa("Maria",26)
```
