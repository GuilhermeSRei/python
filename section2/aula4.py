'''
Escopo de funções em python
Escopo significa o local onde aquele código pode atingir.
Existe o espaço global e local.
O espaço global é o escopo onde todo o código é alcaçabvel.
O escopo local é o escopo onde apenas nomes do mesmo
local podem ser alcançados.
Não temos acesso a nomes de escopo de escopos internos
nos escopos externos.
A palavra global faz uma variavel do escopo externo ser a mesma
no escopo interno.
'''

x = 1


def escopo():
    # global x
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)