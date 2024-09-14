nascimento = int(input('Informe o ano de seu nascimento: '))
anoatual = int(input('Informe o ano atual: '))

idade = anoatual- nascimento

print(f'Sua idade é de {idade} ano(s)')

if idade >= 18:
    print('Parabéns você é maior de idade')

else:
    print('Poxa, você ainda é menor de idade')