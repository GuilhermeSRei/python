# Exercício - Salve sua Classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias da classe com os dados salvos Faça em arquivos

import json

CAMINHO_ARQUIVO = 'atv1_a.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Guilherme', 30)
p2 = Pessoa('Maria', 25)
p3 = Pessoa('Pedro', 40)

db = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():

    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('Fazendo dump')
        json.dump(db, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('Ele é o MAIN')
    fazer_dump()