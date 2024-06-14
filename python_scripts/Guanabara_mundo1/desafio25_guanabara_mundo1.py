#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Entre com o seu nome: ')).strip()
print('Seu nome tem silva? {}' .format('SILVA' in nome.upper()))
