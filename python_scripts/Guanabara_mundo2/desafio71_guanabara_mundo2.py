#Crie um programa que simule um caixa eletrônico.
#O usuário deve inserir o quanto ele quer sacar. O programa deve mostrar em quantas notas será dado o dinheiro.
#Considere que o caixa forneça apenas notas de 50, 20, 10 e 1.

saque=""


while True:

    while not saque.isdecimal():
        saque=str(input("Qual o valor que você deseja sacar?\n OBS.:Por favor, insira valores inteiros.\nR$ ")).strip()

        if not saque.isdecimal():
            print("Entrada inválida.")
    
    saque = int(saque)

    cinq=saque//50
    vinte=(saque%50)//20
    dez=((saque%50)%20)//10
    um=(((saque%50)%20)%10)//1

    break

print(f"Quantidade de notas de R$50: {cinq}")
print(f"Quantidade de notas de R$20: {vinte}")
print(f"Quantidade de notas de R$10: {dez}")
print(f"Quantidade de notas de R$1: {um}")
