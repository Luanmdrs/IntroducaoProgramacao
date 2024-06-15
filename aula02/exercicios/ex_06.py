valor_unit = 1.37
valor_total = 0
quantidade = int(input('Informe quantas maçãs você irá comprar: '))
if quantidade >= 0:
    if quantidade >= 12:
        valor_total = quantidade*valor_unit*0.9
    elif 0 <= quantidade < 12:
        valor_total = quantidade * valor_unit
    print(f'O valor total de {quantidade} maçãs é R${valor_total:.2f}  ')
else:
    print('Quantidade inválida')
