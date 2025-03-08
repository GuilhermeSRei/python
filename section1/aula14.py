#                    Formataçãp basica de String

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{1000.484654684651684:0=-10,.1f}') # = - Força o número aparecer antes dos zeros
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}') # o !r é opicional nessa situação
