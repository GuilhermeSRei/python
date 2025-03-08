#                                            Operações condicionais

# if / elif .... / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

# if pode ser usado sozinho ou pode ser usado com o else

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':              # O elif tem que ter um if e no final um else 
    print('Você saiu do sistena') 
else:                                # O else depende de um if ou elif
    print('Você não digitou nem "entrar" ou "sair".') 

# If, elif, else dependem um do outro

print('Fora dos blocos')
print()
# --------------------------------------------------------------------------------------------------------------------

# EX 2:

condicao1 = False # Se essa condição for True (verdadeira), ela será executada e as demais serão descartadas, aparecendo a mensagem desiginada, como "Código para a condição 1, duas vezes
condicao2 = False # Se essa condição for True (verdadeira), ela será executada e as demais serão descartadas, aparecendo a mensagem desiginada, como "Código para condição 2"
condicao3 = False # Se essa condição for True (verdadeira), ela será executada e as demais serão descartadas, aparecendo a mensagem desiginada, como "Código para condição 3"
condicao4 = False # Se essa condição for True (verdadeira), ela será executada e as demais serão descartadas, aparecendo a mensagem desiginada, como "Código para a condição 4"

if condicao1:
    print('Código para a condição 1')
    print('Código para a condição 1')
elif condicao2:
    print('Códio para a condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para a condição 4')
else:
    print('Nenhuma condição foi atendida')