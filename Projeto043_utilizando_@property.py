# crie uma classe no qual utilizaremos getters
# porem uma dessa configuraçoes tem que ser padronizada

class Caneta:
    def __inti__(self, cor):
        self.cor_tinta = cor

    @property # um metodo que se conporta como um atributo!!!!!!!!!!!!
    def cor(self): 
        return self.cor_tinta # se colocassemos uma string escrita qualquer coisa aqui, iria aparecer nos 'print(caneta.cor)' de fora
                              # o return retorna o valor que a gente quiser
    @property
    def cor_tampa(self):
        return 'preta'                          

caneta = Caneta('Azul'

print(caneta.cor)
print(caneta.cor_tampa
print(caneta.cor
print(caneta.cor_tampa)
