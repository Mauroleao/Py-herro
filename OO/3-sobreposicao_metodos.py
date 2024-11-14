class Pessoa:
    
    def andar(self):
        print('Estou andando')
        
    def falar(self):
        print('Estou falando')
        
        
class Cliente(Pessoa):
    
    def comprar(self):
        print('Estou comprando')  
        
    def andar(self):
        print('Estou gritando')          
        
        
c1 = Cliente()
c1.falar()        