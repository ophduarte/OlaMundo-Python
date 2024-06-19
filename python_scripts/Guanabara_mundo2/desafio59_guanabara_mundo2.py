#Crie um programa que leia dois números e mostre um menu na tela e realize a ação:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa 

choice=6
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("Escolha uma das opções para realizar a operação:")
print("[1] Somar")
print("[2] Multiplicar")
print("[3] Verificar qual é o maior")
print("[4] Reiniciar e entrar com novos números")
print("[5] Fechar o programa")

while choice!=1 and choice!=2 and choice!=3 and choice!=5:
        choice=int(input("Escolha: "))
        if choice == 4:
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))

if choice==1:
        print("Sua escolha foi somar os números.")
        print(f"A soma dos números {n1} e {n2} é igual a {n1+n2}.")

if choice==2:
        print("Sua escolha foi multliplicar os números.")
        print(f"A multiplicação dos números {n1} e {n2} é igual a {n1*n2}.")

if choice==3:
        print("Sua escolha foi somar os números.")
        if n1>n2:
                print(f"Entre os números digitados, {n1} é maior que {n2}.")
        if n2>n1:
                print(f"Entre os números digitados, {n2} é maior que {n1}.")        

print("Finalizando programa...")