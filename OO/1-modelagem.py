class Pessoas:
    possui_boca = True
    possui_olhos = True
    raca = "Ser humano"
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def retorna_nome(self):
        return self.nome    
        
    def logar_sistema(self):
        print(f'{self.retorna_nome}() está logado no sistema')
        
    @classmethod
    def andar(cls):
        cls.pernas = 2
        return None

        
# p1 = Pessoas('Mauro', 35, '123.456.789-00')
# p2 = Pessoas('Livia', 12, '987.654.321-00')

print(Pessoas.possui_boca)
Pessoas.andar()
print(Pessoas.possui_boca)

