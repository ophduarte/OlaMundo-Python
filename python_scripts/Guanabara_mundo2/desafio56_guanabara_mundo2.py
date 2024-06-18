#Crie um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo;
# Qual é o nome do Homem mais velho e
# Quantas mulheres têm menos de 20 anos.

grupo_nome=[]
grupo_idade=[]
grupo_sexo=[]
i=0
j=0

print('Entre com os dados de 4 pessoas :\n', "------"*10)

for count in range (0,4,1):
        grupo_nome.append(str(input("Qual o nome da {}ª: ". format(count+1))))
        grupo_idade.append(int(input("Qual a idade da {}ª pessoa: ". format(count+1))))
        sexo=(int(input("Qual o sexo da {}ª pessoa:\n(1) Masculino \n(2) Feminino \n(3) Outro\nEscolha:". format(count+1))))
        if sexo==1:
            if grupo_idade[count]>j:
                j=grupo_idade[count]
                nome_h= grupo_nome[count]
        if sexo==2 and grupo_idade[count]<20:
                i=i+1

print("\nA média de idade do grupo é {} anos.".format(sum(grupo_idade)/4))
print("O nome do Homem mais velho é: {}" .format(nome_h))
print("A quantidade de mulheres com idade menor que 20 anos é: {}" .format(i))
