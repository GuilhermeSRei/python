'''
Closure e funções que retornam outras funções
'''

def criar_saudacao(saudacao):
    
    def saudar(nome):
        return f'{saudacao}, {nome}!'

    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
Falar_boa_noite = criar_saudacao('Bom noite')

for nome in ['Maria', 'Joanna', 'Mario']:
    print(falar_bom_dia(nome))
    print(Falar_boa_noite(nome))
    print()