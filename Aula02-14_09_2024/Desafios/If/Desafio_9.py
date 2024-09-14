peso = float(input('Insira seu peso(em kg): '))
altura = float (input('Insira sua altura(em cm): '))

imc = peso / ((altura/100)** 2)


print(f'Seu IMC é {imc:.2f} e sua classificação é:')

if imc < 18.5:
    print('Baixo Peso')
elif imc >=18.5 and imc <= 24.9:
    print('Peso Normal')
elif imc >= 25 and imc <= 29.9:
    print('Excesso de Peso')
elif imc >30 and imc <35:
    print('Obesidade')
elif imc >35:
    print('Obesidade Extrema')
