#Peça que o usuário entre com o valor de um imóvel, com o seu salário e em quantos anos ele pretende parcelar o valor do imóvel.
#Caso a prestação do imóvel sejá maior que 30% do salário do usuário, não poderá ser feito um "suposto" empréstimo para comprar o imóvel.
#Caso contrário, mostrar o valor das prestações.

casa = float(input('Digite o valor da casa: ' ).strip())
sal = float(input('Digite o valor do seu salário: ').strip())
ano = float(input('Digite a quantidade de anos: ').strip())

prest = (casa/ano)

if prest>(sal*0.3):
    print('A parcela é maior do que 30% do seu salário.')
    print('Infelizmente não será possível realizar o empréstimo.')
else:
    print('O empréstimo terá parcelas de R${:.2F}.' .format(prest))
