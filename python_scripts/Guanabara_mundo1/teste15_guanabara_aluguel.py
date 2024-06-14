# Entre com o valor de km andados e quantidade de dias. O preço do aluguel é dado por R$60 por dia + R$0.15 por km rodado

km = float(input('Quantos quiolometros (km) foram rodados com o veículo? '))
dia = int(input('Quantos dias o veículo foi usado? ' ))
print('O valor do alugel será de R${:.2f}.' . format((60*dia)+(0.15*km)))

