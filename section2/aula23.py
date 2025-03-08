# dir, hasattr e getattr em python

string = 'Teste'
metodo = 'lower'

print(string)

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método que vc digitou', metodo)
    