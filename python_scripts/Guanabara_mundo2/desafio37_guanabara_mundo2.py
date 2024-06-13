num = int(input('Digite o número decimal que queira converter: ').strip())
base = int(input('Escolha entre as bases: \n1 - Binário\n2 - Octal\n3 - Hexadecimal\nEscolha: '))

if base==1:
    print('{}'.format(bin(num)[2:]))

elif base==2:
    print('{}'.format(oct(num)[2:]))

elif base==3:
    print('{}'.format(hex(num)[2:]))

else:
    print('Essa base não está listada.')
    print('Infelizmente não será possível converter o número.')