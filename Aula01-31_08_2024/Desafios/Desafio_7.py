#Programa conversor de metros para centímetros e milímetros

#Entrada de dados
m = float(input('Digite a distância (em metros): '))

cm = m * 100
mm = m * 1000

#Saída de dados
print(f'{m}m em cm é {cm:.2f}cm e em mm é {mm:.2f}mm')