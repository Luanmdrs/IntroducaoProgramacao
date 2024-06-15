vogais = ['a', 'e', 'i', 'o', 'u']

letra = input('Informe uma letra: ').lower()

if letra in vogais:
    print(f'{letra} é uma vogal.')
else:
    print(f'{letra} é uma consoante.')