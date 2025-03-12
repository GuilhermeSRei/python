# Recarregando modulos, importlib, singleton
import importlib

import aula33_m

print(aula33_m.variavel)

for i in range(10):
    
    importlib.reload(aula33_m)
    print(i)

print('Fim')