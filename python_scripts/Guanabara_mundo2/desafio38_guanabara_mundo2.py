#Peça dois números inteiros para o usuário e determine qual número é maior.
#Caso os números sejam iguais, mostrar que são iguais.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1>n2:
    print('O primeiro número é maior que o segundo.')

elif n1<n2:
    print('O segundo número é maior que o primeiro.')

else:
    print('Os número são iguais.')
    