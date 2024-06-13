peso = float(input('Entre com o valor do seu peso em quilogramas (kg): '))
altura = float(input('Entre com o valor da altura em metros: '))

IMC = peso/(altura**2)
print('O valor de IMC calculado foi de: {:.2f}' .format(IMC))

if IMC<18.5:
    print('abaixo do peso')
elif IMC>=18.5 and IMC<25:
    print('Peso ideal')
elif IMC>=25 and IMC<30:
    print('Sobrepeso')
elif IMC >=30 and IMC<40:
    print('obesidade')
else:
    print('obesidade morbida')