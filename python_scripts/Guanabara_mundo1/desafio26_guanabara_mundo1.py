#Crie um programa que leia uma frase e conte quantas letras "A", em qual posição ela aparece pela primeira e última vez

frase = str(input('Entre com uma frase: ')).upper().strip()
print('A palavra tem {} letras "A".' .format(frase.count('A')))
print('A primeira vez que aparece a letra "A" foi na posição: {}' .format(frase.find('A')+1))
print('A última vez que aparece a letra "A" foi na posição: {}' .format(frase.rfind('A')+1))
