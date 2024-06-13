casa = float(input('Digite o valor da casa: ' ).strip())
sal = float(input('Digite o valor do seu salário: ').strip())
ano = float(input('Digite a quantidade de anos: ').strip())

prest = (casa/ano)

if prest>(sal*0.3):
    print('A parcela é maior do que 30% do seu salário.')
    print('Infelizmente não será possível realizar o empréstimo.')
else:
    print('O empréstimo terá parcelas de R${:.2F}.' .format(prest))