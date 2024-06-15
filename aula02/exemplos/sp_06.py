from time import sleep

print('--- Iniciando o programa ---')
sleep(2)

ano_nascimento = int(input('Informe o ano de nascimento: '))
ANO_ATUAL = 2024

idade = ANO_ATUAL - ano_nascimento

if idade >= 16:
    print('Você pode votar.')
    if idade < 18:
        print('Você não pode dirigir')
    elif idade >= 18:
        print('Você pode dirigir.')
else:
    print('Você não pode votar e nem dirigir.')

print('--- Fim do programa ---')
