#Crie um programa que faça uma PA e mostre os 10 primeiros termos. Utilize o While para fazer o laço de repetição.
i=0
num = int(input("Digite o primeiro termo da Progressão Aritmética: "))
r = int(input("Digite a razão: "))
pa=[str(num)]

while i<9:
        num = num + r
        pa.append(str(num))
        i+=1

print(f"Os 10 primeiros números da PA são: {", ". join(pa)} ")