#Crie um programa que leia a velocidade de um automóvel, se ele ultrapassar 80km/h, será cobrado uma multa de R$7.00 por km/h excedido

vel = float(str(input('Digite a velocidade em km/h: ')).strip())

if vel>80:
    print('Você foi multado. A Multa será no valor de R${:.2f}' .format((vel-80)*7))
    print('Você excedeu a velocidade em {:.2f}km/h.'.format(vel-80))

else:
    print('Parabéns, você estava dentro do limite de velocidade permitido.')
