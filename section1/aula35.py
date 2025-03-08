'''
Imprecisão de numero flutuante
'''
import decimal

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.1f}')

print(round(numero_3, 3)) 
# (numero, casa decimal) - Caso a casa decimal termine em zero, idenpendente da quantidade de casa decimais colocadas no parametro, sempre ira imprimir o numro com uma unica casa.

numero_4 = decimal.Decimal(0.1)
numero_5 = decimal.Decimal(0.7)
numero_6 = numero_4 + numero_5
print(numero_6)