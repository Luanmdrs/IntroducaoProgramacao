from time import sleep

print('--- Iniciando o programa ---')
sleep(2)

sexo = input('Informe seu gênero (M / F): ').upper()

if (sexo == 'M') or (sexo == 'F'):
    altura = float(input('Informe sua altura: '))
    p_ideal = 0
    if sexo == 'M':
        p_ideal = (72.7*altura) - 58
    elif sexo == 'F':
        p_ideal = (62.1*altura) - 44.7
    print(f'Para o gênero {sexo} e a altura {altura:.2f}m, o peso ideal é {p_ideal:.2f}kg.')
else:
    print('O gênero informado é inválido.')


print('--- Fim do programa ---')