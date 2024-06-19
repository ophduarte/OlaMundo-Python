#Crie um programa que faça uma PA e mostre os 10 primeiros termos.
#Pergunte se ele quer continuar a sequência.

i=0
j=9
choice=1

num = int(input("Digite o primeiro termo da Progressão Aritmética: "))
r = int(input("Digite a razão: "))
pa=[str(num)]

while choice != 0:
        while i<j:
                num = num + r
                pa.append(str(num))
                i+=1

        print(f"Os {len(pa)} primeiros números da PA são: {", ". join(pa)} ")

        print("Deseja visualizar a PA com mais termos?")
        choice= int(input("[1] Sim\n[0] Não\nEscolha: "))
        
        if choice == 1:
                j = j + int(input("Acrescentar mais quantos termos? "))


print("Finalizando programa...")