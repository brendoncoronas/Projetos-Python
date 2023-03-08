# faça uma codigo que utilize 3 ou mais funçoes
# utilizar funçoes DECORADORA como funcao principal

def inverte_string(string):
    return string[::-1

def criar_funcao(func:
    def interna(*args, **kwargs:
        print('vou te decorar'
        for arg in args:
            e_string(arg)

        resultado = func(*args, **kwargs)
        print(f'o seu resultado foi {resultado}')
        print('ok, agora voce foi decorada.')
        return resultado
    
    return interna

def e_string(param):
    if not isinstance(param, str): # esse param é definido dentro da funcao 'interna'
        raise TypeError('param deve ser uma string.')

inverte_string_checando_parametros = criar_funcao(inverte_string)     
invertida = inverte_string_checando_parametros('123') 
print(invertida)      
