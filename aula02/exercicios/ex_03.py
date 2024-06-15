num1 = float(input('Informe o primeiro número: '))
num2 = float(input('Informe o segundo número: '))

if num1 == num2:
    print('Os números são iguais.')
else:
    if(num1 > num2):
        print(f'{num1} é maior que {num2}')
    else:
        print(f'{num2} é maior que {num1}')