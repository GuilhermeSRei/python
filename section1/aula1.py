
# Usar comentários para auxiliar nas aulas
''' DocString não é um comentário, mas pode ser usada dessa maneira'''

print(12, 34)
print()

# -----------------------------------------------------------------------

#                  Tipos de Dados

#                      String

'''
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> String -> Texto
String são textos que estão dentro de aspas "" ou ''
'''

# Exemplo
print('Guilherme Reis')
print("Guilherme Reis")
print('Guilherme "Reis"')

# Escape
print("Guilherme \"Reis\"")

# r
print(r"Guilherme \"Reis\"")

print()
# ------------------------------------------------------------------------
#                   Int e Float

# int
# Int -> Número inteiro
# O tipo int representa qualquer número, positivo ou negativo, inteiro.
# O int sem sinal é considerado como positivo

print(1) # Número inteiro positivo
print(-1) # Número inteiro negativo
print(0) # zero também é considerado um número inteiro

print()
# float
# float - > Número com ponto flutuante (Decimal)
# O tipo float representa qualquer número, positivo ou negativo, decimal,
# ou seja, que tenha um número flutuante.
# O float sem sinal é considerado positivo.

print(1.1) # Número decimal/float positivo
print(-1.1) # Número decimal/float negativo
print(0.0) # Número decimal/float 0.0 é considerado float

print()
# Função type
# Essa função determina o tipo de dado
print(type(1)) # Demonstra o tipo de dado, no caso int
print(type('1')) # str (String)
print(type(0.0)) # float

print()
# -------------------------------------------------------------------------
#                  Bool ou Boolean
# 
# Ao questionar algo em um programa, só exidte duas resposta:
# Sim (true) ou Não (false)
# Existe vários operadores para "questionar". Dentre eles tem o ==
# que significa igual á ___.
 
print(10 == 10) # True (Verdadeiro)
print(10 == 11) # False (Falso)
print (type (10 == 10)) # Tipo bool ou boolean   

print()