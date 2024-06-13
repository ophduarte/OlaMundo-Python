aresta1 = float(input('Digite o valor do primeiro lado de um triângulo: ')) 
aresta2 = float(input('Digite o valor do segundo lado de um triângulo: ')) 
aresta3 = float(input('Digite o valor do terceiro lado de um triângulo: '))

if aresta1>aresta2 and aresta1>aresta3:
    maior=aresta1
    
    if aresta2>aresta3:
        meio=aresta2
        menor=aresta3
    
    else:
        meio=aresta3
        menor=aresta2

elif aresta1>aresta2 and aresta1<aresta3:
    maior=aresta3
    meio=aresta1
    menor=aresta2

elif aresta1<aresta2 and aresta1>aresta3:
    maior=aresta2
    meio=aresta1
    menor=aresta3

elif aresta1<aresta2 and aresta1<aresta3:
    if aresta2>aresta3:
        maior=aresta2
        meio=aresta3
        menor=aresta1
    else:
        maior=aresta3
        meio=aresta2
        menor=aresta1
else:
    maior=aresta3
    meio=aresta2
    menor=aresta1

if (menor+meio) >= maior:

    if aresta1==aresta2 and aresta1==aresta3:
        print('Triângulo equilátero')
    elif (aresta1==aresta2 and aresta1!=aresta3) or (aresta2==aresta3 and aresta2!=aresta1) or (aresta1==aresta3 and aresta1!=aresta2):
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')

else:
    print('As dimensões fornecidas não formam um triângulo.')


print('menor: {}\nmeio: {}\nmaior: {}' .format(menor, meio, maior))