#Crie um programa que leia o primeiro termo e a razão de uma PA. Mostre os 10 primeiros termos da PA.
print("Olá, será realizada a Progressão Aritmética que você desejar.")
n1= int(input("Digite o primeiro número da PA: "))
r= int(input("Digite a razão da PA: "))
pa=[n1]

for count in range (1,10,1):
   pa.append(pa[count-1]+r)

print(pa)
