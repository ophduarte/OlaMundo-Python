km = float(str(input('Entre com a distância de sua viagem: ')).strip())

if km<=200:
    print('O valor da passagem será de R${:.2f}.' .format(km*0.5))
    
else:
    print('O valor da passagem será de R${:.2f}.' .format(km*0.45)) 