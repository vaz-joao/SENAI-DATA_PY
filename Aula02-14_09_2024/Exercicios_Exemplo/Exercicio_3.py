media = float(input('Qual a média: '))

print(f'A sua média foi de {media}')

if media<5:
    print('Que pena. Você foi REPROVADO!')

elif media <7:
    print('Calma. Você esta de RECUPERAÇÃO, mas chegará lá!')

else:
    print('Show. Você foi APROVADO!')