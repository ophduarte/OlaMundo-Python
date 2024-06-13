#Faça um programa que leia um número inteiro e mostra o seu antecessor e seu sucessor.

num = int(input('Digite um número inteiro: '))
print('O número digitado foi {}. O antecessor é {}. O sucessor é {}.'.format(num, num-1, num+1))
