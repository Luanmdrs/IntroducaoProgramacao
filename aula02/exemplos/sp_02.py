#situação problema 02

from math import ceil

PI = 3.14
raio = float(input(f'Qual o raio da base do cilindro: '))
altura = float(input(f'Qual a altura do cilindro: '))

area_lateral = 2 * PI * raio * altura
area_base = PI * (raio ** 2)
area_cilindro = area_lateral + area_base
quant_litros = area_cilindro / 3
quant_latas = ceil(quant_litros / 5)
custo = quant_latas * 50

print(f'Quantidade de latas: {quant_latas}')
print(f'O custo para pintar um cilindro de {raio:.2f}m de raio e {altura:.2f}m de altura é R${custo:.2f}')