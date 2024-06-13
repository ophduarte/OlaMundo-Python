#Faça um programa que converta um tamanho em metros para centímetros e milímetros.

metros = float(input('Digite o tamanho em metros (m): '))
print('Convertendo para Centímetros: {}cm. Convertendo para milímetros: {}mm.'.format(int(metros*100), int(metros*1000)))
