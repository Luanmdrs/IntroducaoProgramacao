from time import sleep

print('Iniciando o programa.')

'''A função sleep serve para o programa aguardar a quantidade de segundos definida.'''
sleep(2)
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
ingresso = input('Ingresso VIP ou PISTA? ').upper()



if idade >= 18 and ingresso == 'VIP':
    print(f'{nome}, você pode entrar na festa.')
    print('Siga em direção ao elevador!')
else:
    print(f'{nome}, você não pode entrar na festa.')



print('Finalizando o programa.')