# crie uma classe no qual utilizaremos getters
# porem uma dessa configuraçoes tem que ser padronizada

class Caneta:
    def __inti__(self, cor):
        self.cor_tinta = cor

    @property 
    def cor(self): 
        return self.cor_tinta 
    
    @property
    def cor_tampa(self):
        return 'preta'                          

caneta = Caneta('Azul')

print(caneta.cor)
print(caneta.cor_tampa)
print(caneta.cor)
print(caneta.cor_tampa)
