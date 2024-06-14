#Crie um programa que calcule a hipotenusa de um triângulo. Peça o valor dos dois catentos.

import math
cat1 = float(input('Digite o valor do primeiro cateto: '))
cat2 = float(input('Entre com o valor do segundo cateto: '))
print('A parte inteira do número é: {:.2f}' .format(math.hypot(cat1,cat2)))
