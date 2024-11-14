class Pessoa:
    
    def andar(self):
        print('Estou andando')
        
    def falar(self):
        print('Estou falando')
        
class Cliente(Pessoa):
    
    def comprar(self):
        print('Estou comprando')
        
        
class Vendedor(Pessoa):
    
    def vender(self):
        print('Estou vendendo')        
    
c1 = Cliente()
v1 = Vendedor()

c1.andar()
c1.comprar()
c1.falar()  
v1.vender()
v1.falar()
v1.andar()
