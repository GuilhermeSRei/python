# Introdução aos Packages (pacotes) em python
from sys import path

import aula34_package.modulo
from aula34_package import modulo
from aula34_package.modulo import soma_do_modulo
from aula34_package.modulo import *


# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula34_package.modulo.soma_do_modulo(2, 3))
print(modulo.soma_do_modulo(4, 4))
print(variavel)
# print(nova_variavel)