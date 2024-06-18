#Crie um programa que leia o peso de 5 pessoas e mostre qual é o maior peso e qual é menor peso

pesos=[]
print('Entre com o peso de 5 pessoas :\n', "------"*10)

for count in range (1,6,1):
        pesos.append(float(input("Entre com o peso da {}ª pessoa em quilogramas (kg): ". format(count))))
        
print("A pessoa com maior peso pesa {}kg.\nA pessoa com menor peso pesa {}kg." .format(max(pesos), min(pesos)))
