#Faça um programa que pergunte o salário do usuário.
#Para salários superiores a R#1250.00, mostre o novo salário com aumento de 10%
#Para salários inferiores, mostre o novo salário com aumento de 15%

sal = float(str(input('Entre com o seu salário: ')).strip())
if sal<=1250:
    print('Seu aumento será de 15%.')
    print('Portanto, seu salário que era R${:.2f} passará a ser R${:.2f}.' .format(sal, sal*1.15))
else:
    print('Seu aumento será de 10%.')
    print('Portanto, seu salário que era R${:.2f} passará a ser R${:.2f}.' .format(sal, sal*1.10))
