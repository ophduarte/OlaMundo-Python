#Faça um programa que jogue Jokenpô com o usuário.

import random, time
pc_choice = random.randint(1,3)
if pc_choice==1:
    pc_choice='Pedra'
elif pc_choice==2:
    pc_choice='Papel'
else:
    pc_choice='Tesoura'


user_choice = int(input('Vamos jogar Jokenpo!\nEscolha um entre:\n(1) Pedra \n(2) Papel \n(3) Tesoura\n'))

if user_choice==1:
    user_choice='Pedra'
elif user_choice==2:
    user_choice='Papel'
else:
    user_choice='Tesoura'

print('\nSua escolha VS Computador')
print('--'*5,'Confrontando','--'*5)
time.sleep(2)

if (user_choice=='Pedra' and pc_choice=='Pedra') or (user_choice=='Papel' and pc_choice=='Papel') or (user_choice=='Tesoura' and pc_choice=='Tesoura'):
    print('\n{} VS {}.\nEmpate.\n' .format(user_choice, pc_choice))
    
elif (user_choice=='Pedra' and pc_choice=='Tesoura') or (user_choice=='Papel' and pc_choice=='Pedra') or (user_choice=='Tesoura' and pc_choice=='Papel'):
    print('\n{} VS {}.\nParabéns, você venceu o computador no Jokenpô!!\n' .format(user_choice, pc_choice))

elif (user_choice=='Pedra' and pc_choice=='Papel') or (user_choice=='Papel' and pc_choice=='Tesoura') or (user_choice=='Tesoura' and pc_choice=='Pedra'):
    print('\n{} VS {}.\nQue pena, você perdeu o Jokenpô para o computador.\n' .format(user_choice, pc_choice))
