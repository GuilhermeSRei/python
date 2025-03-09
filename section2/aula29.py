# try, except, else e finally

# Try, except, else e finally não vem sozinho, sempre acompanhado

# try:
#     print('Abrir arquivo')
#     8/0
# finally:
#     print('Fechar arquivo')

#---------------------------------------

# try:
#     print('Abrir arquivo')
#     # 8/0
# except ZeroDivisionError:
#     print('Dividiu zero')
# finally:
#     print('Fechar arquivo')

#---------------------------------------

try:
    print('Abrir arquivo')
    # 8/0
except ZeroDivisionError:
    print('Dividiu zero')
else:
    print('Não deu erro')
finally:
    print('Fechar arquivo')