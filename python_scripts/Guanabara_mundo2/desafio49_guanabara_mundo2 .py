#Crie um programa que faça a tabuada de um número com laço FOR.

num = int(input("Digite o número que queira fazer a tabuada\n"))
for count in range (1,11,1):
    print("{} x {} = {}." .format(num, count, num*count))
