#Programa para calcular quantos litros são necessarios para pintar uma parede

#Solicite o tamanho da parede
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura

consumo = area / 2

#Saída de dados
print(f'Se para cada 1 litro conseguimos pintar 2m², para pintar {area}m² será necessario {consumo:.2f} litros')