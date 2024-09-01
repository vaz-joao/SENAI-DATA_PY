#Programa para Calcúlo de Dissídio

colaborador = input('Informe o seu nome: ')
salarioAtual = float(input('Informe o salário atual: '))

reajuste = salarioAtual * 0.15

salarioNovo = salarioAtual + reajuste

print(f'O salário atual do colaborador {colaborador}, é de {salarioAtual}. O mesmo'
      f'terá um reajuste de {reajuste}, totalizando dessas'
      f'forma um novo salário de {salarioNovo}')