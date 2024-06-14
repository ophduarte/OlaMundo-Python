#Faça um programa que mostre na tela uma contagem regressiva, de 10 a 0, com pausa de 1segundo.

import time

for count in range (10,-1,-1):
    print(count)
    time.sleep(1)
print("Seu tempo acabou!")