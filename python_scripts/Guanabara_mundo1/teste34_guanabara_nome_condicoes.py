sal = float(str(input('Entre com o seu salário: ')).strip())
if sal<=1250:
    print('Seu aumento será de 15%.')
    print('Portanto, seu salário que era R${:.2f} passará a ser R${:.2f}.' .format(sal, sal*1.15))
else:
    print('Seu aumento será de 10%.')
    print('Portanto, seu salário que era R${:.2f} passará a ser R${:.2f}.' .format(sal, sal*1.10))