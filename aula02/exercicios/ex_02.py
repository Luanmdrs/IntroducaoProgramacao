temp = float(input('Insira a temperatura: '))
escala = input('Informe a escala de origem (C / F): ').upper()
resultado = 0

if escala == 'C':
    resultado = temp*1.8 + 32
    print(f'Temperatura em graus fahrenheit: {resultado:.2f}ºF')
elif escala == 'F':
    resultado = (temp - 32)/1.8
    print(f'Temperatura em graus celsius: {resultado:.2f}ºC')
else:
    print(f'Escala {escala} inválida')