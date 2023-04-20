# faça um que mostre o uso claro de

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'chamando', self.phone)


call1 = CallMe('3857617618') # é para ser um numero de celular
call1('brendon coronas')  # sabemos que normalmente isso nao é executavel
# porem com o __call__ torna viavel a execução
