n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

print(f'Sua média foi {media}')

if media >= 0 and media < 5:
    print('Reprovado')

elif media >= 5 and media < 8:
    print('Recuperação')

elif media >= 8 and media <= 10:
    print('Aprovado')