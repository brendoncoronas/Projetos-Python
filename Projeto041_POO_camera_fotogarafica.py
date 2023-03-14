# crie uma classe camera em que ela possa 
# filmar, fotografar, parar de filmar
# e enquanto estiver filmando nossa camera
# nao podera fotografar


class Camera:
    def __init__(self, nome, filmando=False:
        self.nome = nome 
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ esta filmando...')
            return 

        print(f'{self.nome} esta filmando...')
        self.filmando = True


    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO esta filmando...')
            return 

        print(f'{self.nome} esta parando de filmando...')
        self.filmando = False


    def fotografas(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto estiver filmando')
            return 

        print(f'{self.nome} esta fotografando...')
            


c1 = Camera('canon')        
c2 = Camera('sony')
c1.filmar() # alem de começar a filma nos mantemos o valor 
c1.filmar()

print(c1.filmando) # estamos guardando os estados das coisas, ja que filmando de c1 virou True s       
print(c2.filmando)        
