#Faça um programa que leia vários nomes, enquanto o usuário desejar entrar com os nomes.
#Mostre a quantidade de nomes que foram inseridos.

nome=[]
choice=""

while True:
    nome.append(str(input("\nDigite um nome: ")))
    choice=str(input("\nDeseja entrar com outro nome? [S/N]\nEscolha: ")).upper()

    while choice!="S" and choice!="N":
        print("Entrada inválida.")
        choice=str(input("Deseja entrar com outro nome? [S/N]\n Escolha: ")).upper()
    
    if choice=="N":
        break

print(f"\nForam digitados o total de {len(nome)} nomes.\n")
