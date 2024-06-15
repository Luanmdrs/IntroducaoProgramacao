valor_inicial = float(input('Insira o valor do produto: '))
desconto = float(input('Insira o percentual de desconto: '))
desconto_ajustado = desconto/100

valor_final = valor_inicial - valor_inicial*desconto_ajustado

print(f'Valor do produto com desconto: R${valor_final:.2f}')