import random

rand = str(random.randint(0,5))
# print(rand)
num = str(input('Tente acertar o número que foi sorteado, de 0 a 5: ')).strip()

if rand==num:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou.') 