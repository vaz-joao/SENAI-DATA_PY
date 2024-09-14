nome = input('Digite o nome do aluno(a): ')
materia = input(f'Digite o nome da matéria a dar a nota para o(a) aluno(a) {nome}: ')


nota1 = float(input(f'Digite a nota do 1º Bimestre da máteria de {materia} para o(a) aluno(a) {nome}: '))
nota2 = float(input(f'Digite a nota do 2º Bimestre da máteria de {materia} para o(a) aluno(a) {nome}: '))
nota3 = float(input(f'Digite a nota do 3º Bimestre da máteria de {materia} para o(a) aluno(a) {nome}: '))
nota4 = float(input(f'Digite a nota do 4º Bimestre da máteria de {materia} para o(a) aluno(a) {nome}: '))

media = (nota1+nota2+nota3+nota4)/4

print(f'A média final do(a) aluno(a) {nome} na matéria de {materia} foi {media}')
print(f'Nome: {nome}\nMatéria: {materia}\nMédia: {media}')

if media >= 0 and media < 5:
    print('\033[1;31;43mReprovado\033[m')

elif media >= 5 and media < 8:
    print('\033[1;34mRecuperação')

elif media >= 8 and media <= 10:
    print('\033[1;32mAprovado')