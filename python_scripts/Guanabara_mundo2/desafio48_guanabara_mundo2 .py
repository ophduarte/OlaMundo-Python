#Crie um programa que calcule a soma entre todos os números ímpares que são múltiplos de três que estão entre 1 e 500
soma=0
for count in range (1,501,1):
    if count%2==1 and count%3==0:
        print("Número encontrado {}." .format(count))
        soma =soma+count

print("A soma dos números ímpares e múltiplos de 3 é igual a {}." .format(soma))
