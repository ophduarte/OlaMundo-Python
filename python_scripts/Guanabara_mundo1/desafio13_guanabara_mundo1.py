#Faça um programa que leia o salário de um funcionário e mostre o novo salário dele com aumento de 15%

sal = float(input('Digite o salário do funcionário: '))
print('O funcionário receberá um aumento de 15%, recebendo então o valor final de R${}.' .format(round(sal*1.15,2)))