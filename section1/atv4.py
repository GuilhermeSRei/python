# Exercício

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome de invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print(f'Seu nome contém espaço')
    else:
        print(f'Seu nome não contém estaço')

    print(f'Seu nome tem {len(nome)} caracteres')
    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A ultima letra do seu nome é "{nome[-1]}"')
else:
    print(f'Desculpe, você deixou campos vazios')