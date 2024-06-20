#Crie um programa que leia vários números inteiros. O programa funcionará até que o número 999 seja digitado.
#No final, mostre quantos números foram digitados e qual é a soma entre eles.

i=0
count=0
soma=0

while i!=999:
    i=int(input("Digite um número qualquer:"))
    
    if i != 999:
        soma+=i
        count+=1

print(f"Foram digitados {count} números.")
print(f"A soma entre os números digitados foi igual a {soma}")

