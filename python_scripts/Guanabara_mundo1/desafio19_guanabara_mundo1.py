#Crie um programa que peça 4 nomes de alunos e sortei o nome de um deles. 

import random
nome1 = input('entre com o primeiro nome: ')
nome2 = input('entre com o segundo nome: ')
nome3 = input('entre com o terceiro nome: ')
nome4 = input('entre com o quarto nome: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('O aluno sorteado foi: {}' .format(random.choice(lista)))
