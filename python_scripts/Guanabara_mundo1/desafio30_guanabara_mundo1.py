#Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar

num = int(str(input('entre com um número inteiro positivo: ')).strip())

if num%2==0:
    print('O número digitado é par.')
    
else:
    print('O número digitado é ímpar.') 
