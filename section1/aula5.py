
#                                 Formatação de string

nome = 'Guilherme Reis'
altura = 1.74
peso = 79
imc = peso / (altura ** 2)

# f string
linha_1 = f'{nome} tem {altura:.2f} de altura' # f string consegue formatar a linha de maneira       dinâmica

print(linha_1)
print(f'pesa {peso} Kg e seu IMC é {imc:.2f}')
print()
#---------------------------------------------------------------------------------------------------------------

#                                  Formatação com format

a = 'A'
b = 'B'
c = 1.1
string = 'a = {n1}, b = {n2}, c = {n3:.2f}' # --> Usando parametro nomeado
# string = 'a = {0}, b = {1}, c = {2:.2f}' # --> Utiliza indice
#string = 'a = {}, b = {}, c = {:.2f}' # --> Não utiliza nem indice e nem parametro


formato = string.format(n1=a, n2=b, n3=c)
#formato = string.format(a, b, c) # --> sem parametro nomeado


print(formato)