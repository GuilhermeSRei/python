# Módulos padrão do Python (import, from, as, *).

# Import - import nome_modulo
# vantagens -> Você tem namespace do módulo
# desvantagem -> Você tem nomes grandes

import sys

print(sys.platform)
print(sys.exit())

#--------------------------------------------------------

# # From - from nome_modulo import object1, object2
# # vantagens -> Você tem nomes pequenos
# # desvantagem -> sem namespace do módulo

# from sys import exit, platform
# print('Bla')
# print(exit)

#---------------------------------------------------------

# alias 1 - import nome_modulo as apelido:

# import sys as s
# sys = 'Alguma coisa'
# print(sys)
# print(s.platform)

# alias 2 - from nome_modulo import object 1 as apelido:

# from sys import platform as pf, exit as ex
# exit = '1'
# print(exit)
# print(pf)

#----------------------------------------------------------

# má prática - from sys import *

# from sys import *
# print(platform)
# exit()