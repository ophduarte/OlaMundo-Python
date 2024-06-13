#Faça um programa que leia o valor de um produto e mostre o preço final com desconto de 5%

preco = float(input('Digite o preço do produto: '))
print('O produto receberá desconto de 5%, tendo então o valor final de R${}.'. format(round(preco*0.95,2)))
