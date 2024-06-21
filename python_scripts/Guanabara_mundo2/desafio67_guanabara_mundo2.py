#Faça um programa que mostre a tabuada de vários números que o usuário digitar.
#O programa será interrompido quando o usuário inserir um número negativo.
num=""
table=[]
choice=""
i=0

while True:

    while not num.isdecimal():
        num=str(input("Digite um numero inteiro para construir a tabuada:"))
        
        if not num.isdecimal():
              print("O número digitado não é inteiro.")
    
    table.append(int(num))    

    while choice!="N" and choice!="S":
        choice=str(input("\nDeseja digitar outro número? [S/N]\nEscolha:")).upper()
        
        if choice!="N" and choice!="S":
             print("Entrada inválida.\n")
    
    if choice=="S":
        num=""
        choice=""

    if choice=="N":
         break

while i<len(table):
    j=0
    
    print(f"\nTabuada do {table[i]}")
    
    for j in range (0,11,1):
        print(f"{table[i]}x{j} = {table[i]*j}")
    
    print("---"*10)
    
    i += 1
