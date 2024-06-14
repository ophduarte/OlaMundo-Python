#Crie um programa que o usuário tente acertar o número que o computador sorteará entre 0 e 5.

import random

rand = str(random.randint(0,5))

num = str(input('Tente acertar o número que foi sorteado, de 0 a 5: ')).strip()

if rand==num:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou.') 
    