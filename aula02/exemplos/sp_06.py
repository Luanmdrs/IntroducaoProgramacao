from time import sleep

print('Iniciando o programa.')

'''A função sleep serve para o programa aguardar a quantidade de segundos definida.'''
sleep(2)
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

if idade >= 18:
    ingresso = input('Ingresso VIP ou PISTA? ').upper()
    if ingresso == 'VIP':
        print(f'{nome}, você pode entrar na festa.')
        print('Siga em direção ao elevador, para a área VIP!')
    elif ingresso == 'PISTA':
        print(f'{nome}, você pode entrar na festa.')
        print('Siga pelo corredor, para a PISTA!')
    else:
        print(f'{nome}, ingresso inválido.')
else:
    print(f'{nome}, você não pode entrar na festa.')



print('Finalizando o programa.')