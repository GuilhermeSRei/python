# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'C:\\Users\\USER\\Documents\\Estudos\\udemy\\python\\section2\\aula 51 atenção\\'
caminho_arquivo += 'aula51.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     # escrevendo
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'linha 4\n')
#     )

#     # lendo
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     print('readlines')
#     arquivo.seek(0, 0)
#     for linhas in arquivo.readlines():
#         print(linhas.strip())


        
# print('-' * 20)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# ----------------------------------------------------------------
# USO DO 'a'

# with open(caminho_arquivo, 'a+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')

# --------------------------------------------------------------
# encoding

with open(caminho_arquivo, 'r+', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 2\n')
    