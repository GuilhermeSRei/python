
# Sets - conjunto em Python (tipo set)
# Conjunto são ensinados na matemática
# representando graficamente pelo diagrama de Venn
# sets em python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor

# Criando um set
# set(iterável) ou {1, 2, 3}

# Sets saõeficientes para remover valores duplicados
# de iteráveis
# - eles não tem índex;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)


# s1 = set() # Set vazio
# s2 = {'Luiz'} # Set com dados
# print(s1, type(s1))

#-----------------------------------------------------------

# l1 = [1, 2, 3, 3, 3, 4, 3, 5]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)

# s2 = {1, 2, 3, (123),}
# print(s2)

# for numero in s2:
#     print(numero)

#-----------------------------------------------------------

# Métodos Úteis:
# add, update, clear, discard

# s3 = set()

# s3.add('Luiz')
# s3.add(1)
# s3.update(('Olá mundo', 1, 2, 3, 4))
# # s3.clear() # Vai limpar o set
# # s3.discard(3) # Descarta o valor definido

# print(s3)

#------------------------------------------------------------

# Operações úteis:

# s4 = {1, 2, 4, 6}
# s5 = {4, 3, 5, 6, 7}

# # UNIÃO | UNIÃO (UNINON) - Une
# s6 = s4 | s5
# # print(s6)

# # Intersecção & (intersection) - Itens presentes em ambos
# s6 = s4 & s5
# # print(s6)

# # Diferença - Itens presentes apenas no set da esquerda
# s6 = s4 - s5
# # print(s6)

# # Diferença simétrica ^ - Itens que não estão em ambos
# s6 = s4 ^ s5
# print(s6)

#--------------------------------------------------------

# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('parabéns')
        break


    print(letras)

