frutas = ['pêra', 'uva', 'maçã', 'kiwi']
print('Lista de frutas: ')
print(frutas)

frutas[1] = 'abacate'

print('Lista de frutas (alterada): ')
print(frutas)

frutas.insert(2, 'morango')

print('Lista de frutas (inserindo morango): ')
print(frutas)

frutas.append('pitaya')
print('Lista de frutas (inserindo pitaya): ')
print(frutas)

del frutas[0]
print('Lista de frutas (removendo pêra): ')
print(frutas)

print('\n------------------------')
frutas.append('Melancia')
print(frutas)

if 'Melancia' in frutas:
    print(f'Indice de Melancia: {frutas.index('Melancia')}')

print('Removendo a pitaya e a melancia: ')
frutas.remove('pitaya')
frutas.remove('Melancia')
print('Lista de frutas (removido pitaya e e Melancia): ')
print(frutas)