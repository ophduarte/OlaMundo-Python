#Crie um programa que leia vários números inteiros e no final mostre a média entre eles, o menor e o maior número inserido.
#Pergunte ao usuário se ele deseja continuar a digitar números.

choice=0
nums=[]

nums.append(int(input("Digite um número: ")))
while choice != "S" and choice != "N":
    choice=str(input("Deseja inserir outro número? [S/N] ")).upper()
    
    if choice != "S" and choice != "N":
        print("Entrada inválida.")
        print("")

while choice=="S":
    nums.append(int(input("Digite mais um número: ")))
    print("")
    choice=str(input("Deseja inserir outro número? [S/N] ")).upper()
    print("")

print("\n","-----"*10)
print(f"A média dos números digitados é igual a {sum(nums)/len(nums)}")
print(f"O menor número digitado foi: {min(nums)}")
print(f"O maior número digitado foi: {max(nums)}")
print("-----"*10)