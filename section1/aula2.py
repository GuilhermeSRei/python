
# Conversão de tipos, coerção
# type convertion, typecasting. coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool

print(1 + '1') # TypeError -> Tipos diferente não podem ser concatenados ou somados
print(int('1') + 1) # Podem ser somados, devido o uso da classe int(),
             # pois transforma o str em int, podendo realizar tal ação.

# Assim como a classe int(), exite também diversas outras classe, como a float(),
# a bool()

print( float('1') + 1) # float(str) + int = float => 1.0 + 1 = 2.0
print(bool(' ')) # bool(str) => True
print(bool()) # bool => False
print(str(11) + 'b') # str(int) + str = str => '11' + 'b' = 11b