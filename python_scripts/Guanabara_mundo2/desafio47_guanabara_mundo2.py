#Crie um programa que mostra na tela todos os números pares que estão entre 1 e 50.

import time

for count in range (1,51,1):
    if count%2==0:
        print(count)
    time.sleep(0.05)
