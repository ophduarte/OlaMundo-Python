#Crie um programa que leia um número inteiro e diga se ele é um primo.

num = int(input("Digite o número para que seja possível verificar se ele é um número primo: "))
if num==0 or num==1:
     print("Número não é primo")
else:
   counter = 0

   for i in range (1,num+1,1):
      if num%i==0:
            counter=counter+1
      if counter==3:
         break

   if counter<3:
         print("Número é primo")
   else:
         print("Número não é primo")     

