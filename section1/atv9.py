
import os

palavra_secreta = 'margarina'
letras_acertadas = ''
tentativas = 0

while True:
    

    letra_digitada = input('Digite uma letra que pode está na palavra secreta: ')
    tentativas += 1
    

    if len(letra_digitada) > 1:
        print('Por favor digite somente uma letra.')
        continue
    

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta 
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!')
        print(f'A palavra era {palavra_secreta}')
        print(f'{tentativas} tentativas')

        letras_acertadas = ''
        tentativas = 0



    
    
