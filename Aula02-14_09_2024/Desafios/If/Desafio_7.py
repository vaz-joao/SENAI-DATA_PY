'''Desenvolva um programa que recebe do usuário, o placar de
um jogo de futebol (os gols de cada time) e informa se o resultado foi um
empate, se a vitória foi do primeiro time ou do segundo time.'''

time1 = int(input('Digite quantos gols o primeiro time fez: '))
time2 = int(input('Digite quantos gols o segundo time fez: '))

if time1 == time2:
    print(f'O jogo empatou em {time1} X {time2}')

elif time1 > time2:
    print(f'A vitória foi do primeiro time que venceu de {time1} X {time2}')

else:
    print(f'A vitória foi do segundo time que venceu de {time2} X {time1}')