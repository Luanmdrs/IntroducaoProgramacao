peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

imc = peso/(altura*altura)

print(f'Com base no seu peso de {peso:.2f}kg e altura de {altura:.2f}m, seu IMC é {imc:.2f}.')