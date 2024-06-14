#faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1= int(str(input('Entre com o primeiro número: ')).strip())
n2= int(str(input('Entre com o segundo número: ')).strip())
n3= int(str(input('Entre com o terceiro número: ')).strip())
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
print('O maior número é o {}, o número intermediário é o {} e o menor número é o {}.' .format(lista[0], lista[1], lista[2]))