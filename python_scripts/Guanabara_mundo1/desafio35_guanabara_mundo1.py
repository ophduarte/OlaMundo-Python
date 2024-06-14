#Faça um programa que receba os valores de 3 retas e verifique se é possível fazer um triângulo.

n1= int(str(input('Entre com o tamanho da primeira reta: ')).strip())
n2= int(str(input('Entre com o tamanho da segunda reta: ')).strip())
n3= int(str(input('Entre com o tamanho da terceira reta: ')).strip())
lista = [' ',' ',' ']

if n1>n2:
    if n2>n3:
        lista[0]=n1
        lista[1]=n2
        lista[2]=n3
    elif n3>n1:
        lista[0]=n3
        lista[1]=n1
        lista[2]=n2
    else:
        lista[0]=n1
        lista[1]=n3
        lista[2]=n2      
elif n1>n3:
    lista[0]=n2
    lista[1]=n1
    lista[2]=n3
else:
    if n2>n3:
        lista[0]=n2
        lista[1]=n3
        lista[2]=n1
    else:
        lista[0]=n3
        lista[1]=n2
        lista[2]=n1

if (lista[1]+lista[2])>=lista[0]:
    print('É possível fazer um triângulo.')
else:
    print('Não será possível fazer um triângulo.')