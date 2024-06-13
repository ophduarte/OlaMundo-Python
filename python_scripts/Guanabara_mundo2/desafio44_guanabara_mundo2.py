preco = float(input('Preço do produto: ').strip())
pagamento = int(input('Escolha a forma de pagamaento:\n(1)À vista no dinheiro\n(2)À vista no cartão\n(3)Em até 2x no cartão\n(4)Em até 3x no cartão\nQual é o modo de pagamento escolhido:'))
if pagamento==1:
    print('\nO produto recebeu desconto de 15%.')
    print('O valor do produto era R${:.2f} e agora é R${:.2f}.\n' .format(preco, preco*0.85))
elif pagamento==2:
    print('\nO produto recebeu 5% de desconto de')
    print('O valor do produto era R${:.2f} e agora é R${:.2f}.\n' .format(preco,preco*0.95))
elif pagamento==3:
    print('\nO produto será parcelado em 2x')
    print('O valor do produto é de R${:.2f}.\nSerão 2 parcelas de R${:.2f}.\n' .format(preco, preco/2))

elif pagamento==4:
    print('\nO produto foi parcelado em 3x, tendo acréscimo de 20% de juros.')
    print('O valor do produto era R${:.2f} e agora tem o total de R${:.2f}.' .format(preco, preco*1.2))
    print('Serão 3 parcelas de R${:.2f}.\n' .format(preco*1.2/3))