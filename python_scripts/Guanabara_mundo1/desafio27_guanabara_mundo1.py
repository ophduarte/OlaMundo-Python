#Faça um programa que leia o nome completo do usuário e mostre o primeiro e o segundo nome

nome = str(input('Entre com seu nome: ')).strip().split()
print('Seu primeiro nome é {} e o seu último sobrenome é {}.' .format(nome[0],nome[(len(nome)-1)]))
