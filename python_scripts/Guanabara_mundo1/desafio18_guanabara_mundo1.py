#Crie um programa que peça um ângulo e calcule o seno, cosseno e a tangente.

import math
ang = math.radians(float(input('Digite com o valor do ângulo: ')))
print('O seno do ângulo é {:.2f}.' .format(math.sin(ang)))
print('O cosseno do ângulo é {:.2f}.' .format(math.cos(ang)))
print('A tangente do ângulo é {:.2f}.' .format(math.tan(ang)))
