from time import sleep

print('--- Iniciando o programa ---')
sleep(2)

sexo = input('Informe seu gênero (HOMEM / MULHER): ').upper()
altura = float(input('Informe sua altura: '))

if sexo == 'HOMEM':
    p_ideal = (72.7*altura) - 58
    print(f'Seu peso ideal é {p_ideal:.2f}kg.')
elif sexo == 'MULHER':
    p_ideal = (62.1*altura) - 44.7
    print(f'Seu peso ideal é {p_ideal:.2f}kg.')
else:
    print('O gênero informado é inválido.')


print('--- Fim do programa ---')