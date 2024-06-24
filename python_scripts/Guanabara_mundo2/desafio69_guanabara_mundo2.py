#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá se o usuário que ou não acrescentar mais pessoas.
#No final mostre: quantas pessoas tem mais de 18 anos, quantos homenes foram cadastrados e quantas mulheres tem menos de 20 anos.

maiores=0
homens=0
mulheres_maiores=0
choice=0
idade_usr=""
sexo_usr=""

while True:
    while not idade_usr.isdecimal():
        idade_usr=str(input("Digite a idade: "))
        
        if not idade_usr.isdecimal():    
            print("Entrada inválida.")
    
    while sexo_usr!="M" and sexo_usr!="F": 
        sexo_usr=str(input("Digite o sexo: [M/F]")).upper()

        if sexo_usr!="M" and sexo_usr!="F":
            print("Entrada inválida.")
    
    if sexo_usr=="M":
        homens+=1

    elif sexo_usr=="F" and int(idade_usr)<20:
        mulheres_maiores+=1
    
    if int(idade_usr)>18:
        maiores+=1

    while choice!="S" and choice!="N":
        choice=str(input("Deseja continuar? [S/N]\n")).upper()

        if choice!="S" and choice!="N":
            print("Entrada inválida.")
    
    if choice == "S":
        idade_usr=""
        sexo_usr=""
        choice=""
    else:
        break

print(f"A quantidade de pessoas maiores de idade cadastrados foi de: {maiores}")
print(f"A quantidade de homens cadastrados foi de: {homens}")
print(f"A quantidade de mulheres com idade inferior a 20 anos cadastradas foi de: {mulheres_maiores}")