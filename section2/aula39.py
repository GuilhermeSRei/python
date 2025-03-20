# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar". 

# Função decoradora
def cria_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)

        resultado = func(*args, **kwargs)
        print('Ok, foi decorada')
        return resultado
    return interna

#-----------------------------------------------------------

@cria_funcao # DECORADOR
def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')


invertida = inverte_string('Guilherme')
print(invertida)