#Crie um programa que leia um número e faça seu fatorial

num = int(input("Digite o número que queria fazer o fatorial: "))
fat=[str(num)]
for i in range (num-1,0,-1):
        num=i*num
        fat.append(str(i))
print(f"{fat[0]}! = {"x".join(fat)} = {num}")