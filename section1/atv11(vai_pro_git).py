'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e lista valores da sua lista
Não permita que o programe quebre com erros
de ídice inexistentes na lista
'''
import os

lista_de_compras = []

while True:
    # os.system('cls')
    menu = input(f'Selecione a opção \n[i]inserir [a]pagar [l]istar: ')
    
    if menu == 'i':
        
            os.system('cls')
            valor = input('Digite o item que deseja adicionar: ')
            if valor != '':
                lista_de_compras.append(valor)
                # print(lista_de_compras)

            else:
                print(f'Não foi acrescentada nenhum valor na lista')
    
    elif menu == 'l':

        os.system('cls')
        if lista_de_compras != []:
            for indice, valor in enumerate(lista_de_compras):
                print(indice, valor)
                
        else:
             print(f'A lista está vazia, por favor acrescente algo')

    elif menu == 'a':
         
        os.system('cls')

        indice_str = input('Digite o índice do item que deseja apagar: ')
        
        try: 
            indice = int(indice_str)
            del lista_de_compras[indice]
            print(f'Lista atualizada: \n{lista_de_compras}')
        except ValueError:
            print('Não foi encontrado este índice')
        except IndexError:
            print('Indice não existe')
        except Exception:
            print('Erro desconhecido')
        
        