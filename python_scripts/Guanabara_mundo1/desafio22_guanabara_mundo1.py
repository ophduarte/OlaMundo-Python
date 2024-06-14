#Crie um programa que leia o nome do usuário e mostre o nome dele formatado, em maíusculo, minúsculo e capitalizado.

nome = input('Digite seu nome inteiro: ')
print('A quantidade de caracteres totais, considerando até espaços: {}' .format(len(nome)))
print('O nome todo em letras maiúsculas: {}.' .format(nome.upper()))
print('O nome todo em letras minúsculas: {}.' .format(nome.lower()))
print('A quantidade de letras sem considerar espaços: {}.' .format(len(nome)-nome.count(' ')))
sep = nome.split()
print('A quantidade de letras da primeira palavra é: {}.' .format(len(sep[0])))
