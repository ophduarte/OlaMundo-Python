# Crie um programa de conversão de temperatura de °C para °F e K

temp = float(input('Entre com o valor da temperatura em Celsius: '))
print('A temperatura {}°C convertida em Fahrenheit é de: {}°F. Já convertida em Kelvin, a temperatura é de: {}K' . format(temp, (temp*(9/5))+32, temp+273.15))
