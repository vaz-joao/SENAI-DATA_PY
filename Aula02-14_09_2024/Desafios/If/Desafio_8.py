idade = int(input('Digite a idade do nadador(a): '))

if idade >=5 and idade <=7:
    print('Infantil A')
elif idade >=8 and idade <=11:
    print('Infantil B')
elif idade == 12 or idade == 13:
    print('Juvenil A')
elif idade >=14 and idade <=17:
    print('Juvenil B')
elif idade >= 18:
    print('Adultos')