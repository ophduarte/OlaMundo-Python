#Crie um programa que leia seis números inteiros e mostre a soma daqueles que forem pares.

print("Olá, serão necessários 6 números inteiros para realizar esse exercício.")
num=["","","","","",""]
soma=0

for count in range (1,7,1):
    num[count-1] = int(input("Digite o {}º número: ".format(count)))
    if num[count-1]%2==0:
        soma=soma+num[count-1]

print("A soma dos números pares digitados é: {}." .format(soma))
