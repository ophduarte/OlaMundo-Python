#Faça um programa que leia um número e apresente seu dobro, o seu tríplo e sua raíz quadrada.

num = int(input('Digite um número inteiro positivo: '))
print('O número digitado foi {}. O dobro dele é {}. O triplo dele é {}. A raiz quadrada dele é {:.2F}.'.format(num, num*2, num*3, num**(1/2)))
