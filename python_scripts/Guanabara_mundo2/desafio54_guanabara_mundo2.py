#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores.

print('Entre com o nome de 7 pessoas e suas respectivas idades:\n')
menores=[]
maiores=[]

for count in range (1,8,1):
        nome_input = str(input("Digite o {}º nome: " .format(count))).strip()
        idade_input = int(input("Qual a idade de {}? " .format(nome_input)))

        if idade_input<18:
                menores.append(nome_input)
        else:
                maiores.append(nome_input)

print("---"*10,"\nForam inseridos {} maiores de idade. \nOs maiores de idade são: \n{}".format(len(maiores),'\n'.join(maiores)))
print("---"*10,"\nForam inseridos {} menores de idade. \nOs menores de idade são: \n{}".format(len(menores),'\n'.join(menores)))
