
vel = float(str(input('Digite a velocidade em km/h: ')).strip())

if vel>80:
    print('Você foi multado. A Multa será no valor de R${:.2f}' .format((vel-80)*7))
    print('Você excedeu a velocidade em {:.2f}km/h.'.format(vel-80))

else:
    print('Parabéns, você estava dentro do limite de velocidade permitido.') 