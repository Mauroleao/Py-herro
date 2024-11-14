# Orientação a Objetos (OO) é um paradigma de programação que utiliza "objetos" e suas interações
# para projetar e programar aplicações de software. Os principais conceitos da OO são:

# 1. Classe: É um modelo ou uma descrição de um conjunto de objetos com características e comportamentos similares.
#    Uma classe define atributos (dados) e métodos (funções) que os objetos da classe terão.

# 2. Objeto: É uma instância de uma classe. Um objeto é criado a partir de uma classe e pode ter seus próprios valores
#    para os atributos definidos na classe.

# 3. Encapsulamento: É o conceito de esconder os detalhes internos de um objeto e expor apenas o que é necessário
#    para o uso do objeto. Isso é feito através de modificadores de acesso (público, privado, protegido).

# 4. Herança: É o mecanismo pelo qual uma classe (subclasse) pode herdar atributos e métodos de outra classe (superclasse).
#    Isso promove a reutilização de código e a criação de hierarquias de classes.

# 5. Polimorfismo: É a capacidade de um objeto ser tratado como instância de diferentes classes, desde que essas classes
#    estejam relacionadas por herança. Isso permite que métodos com o mesmo nome possam ter comportamentos diferentes
#    dependendo do objeto que os invoca.

# Exemplo básico de uma classe em Python:

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

# Criando objetos das classes
cachorro = Cachorro("Rex")
gato = Gato("Mimi")

print(cachorro.nome)  # Output: Rex
print(cachorro.fazer_som())  # Output: Au Au
print(gato.nome)  # Output: Mimi
print(gato.fazer_som())  # Output: Miau