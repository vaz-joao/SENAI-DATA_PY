#Programa para calcular

#Solicite o tamanho da parede
produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))

desconto = preco * 0.05
ValorFinal = preco - desconto

#Saída de dados
print(f'O valor cheio do {produto} é {preco}. Foi aplicado um desconto'
      f'de {desconto}, gerando um valor final de {ValorFinal}')